Cadet 
=======================

Each language team has a copy of Cadet for use during the workshops. 

```
arabic.slovo.world
chinese.slovo.world 
kanbun.slovo.world
kannada.slovo.world
turkish.slovo.world
quechua.slovo.world
russian.slovo.world
tigrinya.slovo.world
yiddish.slovo.world
yoruba.slovo.world 
```

### Overview of Cadet 

<iframe width="560" height="315" src="https://www.youtube.com/embed/yoUQLLzOC_E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Main Page 

<iframe width="560" height="315" src="https://www.youtube.com/embed/YslpG8f79jg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Steps One to Three

<iframe width="560" height="315" src="https://www.youtube.com/embed/BJn7bFiBCpA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

### Steps Four to Six 


<iframe width="560" height="315" src="https://www.youtube.com/embed/RXEZ4YLFxs8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


---

### How do you add new punctuation in spaCy? 

So the idea is that there are different types of punctuations relevant for tokenization. It is described in the spacy documentation: https://spacy.io/usage/linguistic-features#tokenization

There are Prefix, Suffix and Infix:
Tokenizer exception: Special-case rule to split a string into several tokens or prevent a token from being split when punctuation rules are applied.
Prefix: Character(s) at the beginning, e.g. $, (, ", ¿.
Suffix: Character(s) at the end, e.g. km, ), ", !.
Infix: Character(s) in between, e.g. -, --, /, ….
In the punctuation file in cadet, you see something like this:
```
_prefixes = BASE_TOKENIZER_PREFIXES
_suffixes = BASE_TOKENIZER_SUFFIXES
_infixes = BASE_TOKENIZER_INFIXES
TOKENIZER_PREFIXES = _prefixes
TOKENIZER_SUFFIXES = _suffixes
TOKENIZER_INFIXES = _infixes
```

and you can extend all the lists from the base_tokenizer_* with with additional characters. To see how this might look like, here is the english punctuations from the existing spacy model
https://github.com/explosion/spaCy/blob/master/spacy/lang/en/punctuation.py
there, you see that `LIST_ELLIPSES`  is added to the `_infixes`. And this is what LIST_ELLIPSES  looks like:
`LIST_ELLIPSES = [r"\.\.+", "…"]`