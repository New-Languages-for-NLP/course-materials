The spaCy Language Object
=======================

One of the most important things to learn about and understand in the process of adding a language to spaCy is the Language object.  

While Cadet provides a convenience layer for creating a new language object, it is essential that you understand how Language works and how to create and configure it. 

**__init__.py**
You new language is defined in the module's init file. For example:

```python 
@spacy.registry.languages("yo")
class Yoruba(Language):
    lang = "yo"
    Defaults = YorubaDefaults
```

Your Language is a Python object that inherits all the attributes from spaCy's base Language object: `class Yoruba(Language)`. The decorator [`@spacy.registry...`](https://nightly.spacy.io/api/top-level#registry) connects your new language to spaCy so that it knows that a new language has been added.  But what is YorubaDefaults?


