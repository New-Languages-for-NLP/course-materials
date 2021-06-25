Universal features
=======================

The Universal Dependencies site offers an essential handbook and reference on the UD standards.  The section on [universal features](https://universaldependencies.org/u/feat/index.html) can be useful when annotating the morphological features of the tokens in your texts.

For example:  
```html
ID  FORM    lemma   pos xpos    feats
221	Claudia	Claudia	PROPN	_	NounType=Prop|Number=Sing	_	_	_	_
222	rolls	roll	VERB	_	Number=Sing|Person=Three|Tense=Pres|VerbForm=Fin	_	_	_	_
223	her	she	PRON	_	Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs	_	_	_	_
224	eyes	eye	NOUN	_	Number=Plur	_	_	_	_

```
The features column allows you to mark important aspects of the token such as its case, number, tense and form. 
The syntax for features is a UD feature label (such as `Number`) followed by an equal sign and then the value.  If you have several features, they should be ordered alphabetically and separated by a pipe (`|`).

- A full list of features can be found here: https://universaldependencies.org/u/feat/index.html
- Further details on feature standards can be found here: https://universaldependencies.org/format.html#morphological-annotation