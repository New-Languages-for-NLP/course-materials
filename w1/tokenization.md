Tokenization
=======================

From your computer’s perspective, text is nothing more than a sequence of characters. If you ask Python to iterate over a snippet of text, you’ll see that it returns just one letter at a time. Note that the index starts at 0, not 1 and that spaces are part of the sequence. 

```python
text = "Siberia has many rivers."
for index, char in enumerate(text):
    print(index, char)
```
```
0  S
1  i
2  b
3  e
4  r
5  i
6  a
7  
8  h
9  a
10 s
11  
12 m
13 a
14 n
15 y
16  
17 r
18 i
19 v
20 e
21 r
22 s
23 .
```

When we ask Python to find a word, say “rivers”, in a larger text, it is actually searching for a lower-case “r” followed by “i” “v” and so on. It returns a match only if it finds exactly the right letters in the right order.  When it makes a match, Python’s .find() function will return the location of the first character in the sequence. For example:

```python
text = "Siberia has many rivers."
text.find("rivers")
```
```
17
```

Keep in mind that computers are very precise and picky.  Any messiness in the text will cause the word to be missed, so `text.find("Rivers")` returns -1, which means that the sequence could not be found. You can also accidentally match characters that are part of the sequence, but not part of a word.  Try `text.find("y riv")`.  You get 15 as the answer because that is the beginning of the “y riv” sequence, which is present in the text, but isn’t a thing that you’d normally want to find. 

## Natural language processing & Tokenization

While pure Python is sufficient for many tasks, natural language processing (NLP) libraries allow us to work computationally with the text as language. NLP reveals a whole host of linguistic attributes of the text that can be used for analysis.  For example, the machine will know if a word is a noun or a verb with part of speech tagging.  We can find the direct object of a verb to determine who is speaking and the subject of that speech.  NLP gives your programs an instant boost of information that opens new forms of analysis. 

Our first NLP task is tokenization. This is where our text is split into meaningful parts; usually word tokens, spans ("New York City") or sentences. The sentence, “Siberia has many rivers.” can be split into five tokens: ```<Siberia><has><many><rivers><.>```  Note that the ending punctuation is now distinct from the word rivers. The rules for tokenization depend on the language your are using. For English and other languages with spaces between words, you often get good results simply by splitting the tokens on spaces. However, a host of rules are also needed to separate punctuation from a token, to split and normalize words (ex. "Let's" = "Let us") as well as specific exceptions that don't follow regular patterns. 

The [spaCy documentation](https://spacy.io/usage/linguistic-features/#tokenization) is really excellent on this topic and I recommend that you start there. When you're done come back and we'll cover some practical topics and processes that you'll need when creating a new language object. 

## spaCy's Tokenizer 

spaCy's tokenization begins by splitting tokens on spaces. It's nearly identical what you'd get from `"Siberia has many rivers.".split()`, which is `['Siberia','has','many','rivers.']`  Keep a close eye on the period in this sentence. On its own, Python has trouble identifying the period as a distinct token. 

To address this problem, spaCy has rules for how to split these chunks into tokens. In this case, it has a list of punctuation symbols.  If any of those symbols are at the end of a chunk, a suffix rule separates the word from the punctuation.  These rules cover a lot of ground and are very powerful. However, there are many cases where we need to tell spaCy to handle things differently.   

Exceptions are a list of patterns to look for and what to do with them. The exceptions for your language are most often found in `spacy/lang` directory in a `tokenizer_exceptions.py` file. For example, here are the exceptions for English to handle shortened forms of `you all` such as `y'all`. These exceptions cause the tokenizer to split the "y'all" into two tokens. 


__[tokenizer_exceptions.py](https://github.com/explosion/spaCy/blob/34e13c1161f7d42b961026b12d2eb3d3165bae27/spacy/lang/en/tokenizer_exceptions.py#L361)__

```python
"y'all": [{ORTH: "y'", NORM: "you"}, {ORTH: "all"}],
"yall": [{ORTH: "y", NORM: "you"}, {ORTH: "all"}],
```

Note that the spaCy developers have accounted for the most common variations of 'you all' and deliberately decided to incorporate slang and idiomatic usage. They have added a normalized form (NORM). If we're interested in word frequencies and not variation, this can be a very useful. This is available to you as `token.norm_`.     

If you look at the `tokenizer_exceptions.py` files for the existing languages, you'll see a wide range of exceptions and ways of writing the rules. For the sake of simplicity, we'll discuss the two most common ways to add exceptions for your language.

> What are ORTH and NORM? They are token attributes. When your exception becomes a token, it will have a `token.text` attribute: that's ORTH. NORM is `token.norm_` LEMMA is `token.lemma_`, `IS_STOP:True` will mark the token as a stop word; `token.is_stop`.

## Adding new exceptions for your language 

spaCy comes with a lot of opinions and defaults right from the beginning.  In most cases, this will save you time. You can find the default tokenizer exceptions by importing them.  

```python
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS
```

You'll find that `BASE_EXCEPTIONS` is a Python dictionary. 
```python
...
 'C++': [{65: 'C++'}],
 'a.': [{65: 'a.'}],
 'b.': [{65: 'b.'}],
 ... 
```

If one of the base exceptions is causing problems for your language, it's easy to remove it. To remove the `'C++'` exception above:  

```python 
BASE_EXCEPTIONS.pop('C++')
```

spaCy also comes with a nice utility function that lets you add new exceptions to the defaults: `update_exc()`.

For clarity, we will refer to two types of exceptions.  The first are specific, or one-time, exceptions.  These define a very specific pattern for spaCy to look for. If it finds a match, it will apply specific tokenization rules to it. In the example above, `'Cuz` would normally be split into `<'><Cuz>` because the spaCy defaults would treat `'` as a prefix. To prevent this, we can add a specific exception in `tokenizer_exceptions.py`  

Rule-based exceptions look for more general patterns. For the example above, we could add an exception for any time we find `'` followed by the letter c. This would be much more flexible and catch more variations on the form. Instead of 8 specific rules, we'd have one pattern.  But be careful, our rule-based pattern would also apply to `'cuse me!` which is a shortened form of `excuse me!` That might be a good thing, it might not. 

The lesson here is that it's up to you when to use specific exceptions and when to use rule-based exceptions.      

## Specific Exceptions 

To add a new exception, pass a dictionary with a key with the string to match and a list with instructions on how to transform it.

For example:
"BIG YIKES" would normally be split into two tokens `<BIG><YIKES>`. To prevent this from happening, we can create an exception. 

```python
from spacy.symbols import ORTH
from spacy.util import update_exc
         #'match':   [{what to do }]
yikes = {'BIG YIKES':[{ORTH: 'BIG YIKES'}]}
TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, yikes)


```
Let's test to confirm that our the tokenizer is acting as we'd expect. 

```python 
from spacy.lang.en import English
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS

#Load the basic English language object
nlp = English() 

#Here's our new exception
yikes = {'BIG YIKES':[{ORTH: 'BIG YIKES'}]}

#Update the default tokenizer with our tokenizer exception
nlp.tokenizer.rules = update_exc(BASE_EXCEPTIONS, yikes)

doc = nlp("Yikes! BIG YIKES!")
assert doc[2].text == "BIG YIKES"
```

```
[ t for t in doc]
[Yikes, !, BIG YIKES, !]
```

That's exciting! We've made a change to the tokenization rules and it worked. Just keep in mind that exceptions are very specific.  If we have `"Yikes! BIG yikes!"`, we get "BIG" and "yikes" as separate tokens because "yikes" isn't all in caps. Yes, it's that picky. When adding specific exceptions, you'll want to add rules for all of the variations that your model is likely to encounter.  

To build on our momentum, let's discuss several other common types of tokenizer exceptions.


## Separate a word into two tokens 

It's very common to have words that should be split into separate tokens, but there isn't a regular infix that will make the cut.  Here we need an exception. As an example, let's explore Kummerspeck ('grief bacon') the German name for weight from emotional eating.

Here we can use the exceptions list to split the word into parts and detail how to handle each of the new tokens: `'matchword':[{match}{word}]` 

```python
grief_bacon = {'Kummerspeck':[{ORTH:"Kummer"},{ORTH:"speck"}]}
```

```python
from spacy.lang.de import German
nlp = German()
nlp.tokenizer.rules = update_exc(BASE_EXCEPTIONS, grief_bacon)

doc = nlp("Das Problem ist nur, dass das Gewicht, das McCoy sich anfuttert, nicht nur beruflich bedingt ist, sondern mindestens zur Hälfte aus Kummerspeck besteht.")

assert doc[25].text == 'Kummer' and doc[26].text == 'speck'
```

The three use cases covered above are the most common types of tokenizer exceptions: adding normalizations, combining words, splitting words. Exceptions can be extremely useful for one-time problems for which there just aren't any rules or common patterns. However, it's simply impractical to handle everything with specific exceptions. The next section cover ways that you can handle common patterns and rule-based exceptions.   

## Rule-based exceptions 

To handle regular patterns, spaCy has three kinds of rule-based exceptions. They are:

- Prefix: A section at the start of a word that should be separated into its own token.
- Infix: A section in the middle of a word that should be separated into its own token.
- Suffix: A section at the end of a word that should be separated into its own token.

spaCy comes with default rule-based exceptions that can often be found in the language's `punctuations.py` file. Additionally, there is a `spacy/lang/punctuation.py` file that has base `TOKENIZER_PREFIXES`, `TOKENIZER_SUFFIXES`, and `TOKENIZER_INFIXES`; [see here](https://github.com/explosion/spaCy/blob/master/spacy/lang/punctuation.py). These defaults are lists of exception patterns. If you look at the files, you'll see some variety.  Some are just a string such as "$" as a prefix for dollars. '$100' will be split into `<$><100>`. Another approach is to work by charachter type.  For example we could just add `LIST_CURRENCY` as a prefix.  Now spaCy will separate all of the listed currency symbols for you ('$', '£', '€', '¥', '฿'...). There's a large menu of charachter types available to you in [char_classes.py](https://github.com/explosion/spaCy/blob/master/spacy/lang/char_classes.py).   

```python
from spacy.lang.char_classes import LIST_CURRENCY

TOKENIZER_PREFIXES = (
    LIST_CURRENCY
)
```

A third approach uses regular expressions. Regex is a serious pain in the butt.  There are regex masters out there, but most people Google helplessly until they get it to work.  A very helpful resource is [regex101](https://regex101.com/).  This is a website that let's you build a regular expression see its matches in a text.  There are also very helpful explainations to get you started. For the current example, we want to create a tokenization exception for a `$` followed by numbers.  One way of expressing that is `"\$\d*"`, which will match any string with the charachter `$` followed by digits (`\d`) repeating any number of times (`*`).  If you try it out in regex101, you'll see that we get matches on `$1`, `$10000` and `$10000000`.  

```python
TOKENIZER_PREFIXES = (
    r"\$\d*" 
)
```
Wondering what the r is for?  It's Python's raw string, which treats a backslash as a literal character and won't mistake it for a new line \n or tab \t or other escape charachters with a `\` in them. 

We can also add a rule for all of the currency symbols
```python
from spacy.lang.char_classes import CURRENCY

TOKENIZER_PREFIXES = (
    r"\{c}\d*".format(c=CURRENCY)
)
```
The code above will take each individual symbol in CURRENCY and add a regular expression rule for it by replacing {c} with the symbol.   

## Extending defaults

As you develop a language object for a new language, you can delegate much of the work to the existing defaults, but it's quite likely that your language has its own specific symbols and charachters. You can add them to your language's `punctuation.py` file.

For example, the default list of currency symbols does not include the Sheckel ₪. We can add our new prefix by adding a list of new symbols to our TOKENIZER_PREFIXES. 

```python 
from spacy.lang.punctuation import TOKENIZER_PREFIXES as BASE_TOKENIZER_PREFIXES

TOKENIZER_PREFIXES = BASE_TOKENIZER_PREFIXES + ["₪"]
```

The prefixes are added to the language object in `__init__.py`

### Prefixes in action

The addition of prefixes will usually be added to the language object. However, you may want to make adjustments on the fly. It's also a good way to check that the new prefix is really what you need [docs](https://spacy.io/usage/linguistic-features#native-tokenizer-additions).

```python
from spacy import util
from spacy.lang.he import Hebrew

nlp = Hebrew()

prefixes = nlp.Defaults.prefixes + ['₪']
prefix_regex = util.compile_prefix_regex(prefixes)
nlp.tokenizer.prefix_search = prefix_regex.search

doc = nlp("₪181 בלבד! משלוח חינם!") #"Only NIS 181! Free Shipping!"
[t for t in doc]
```

```
[₪, 181, בלבד, !, משלוח, חינם, !]
```
Extra brain teaser: Hebrew is written from right to left, so why isn't ₪ a suffix? 
spaCy works well with RTL langauges, but the tokenizer moves from left to right.  Even though ₪ follows 181 in the sentence, spaCy considers it a prefix.   
