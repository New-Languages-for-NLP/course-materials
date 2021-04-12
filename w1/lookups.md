Lookups Data
=======================

While spaCy can learn to predict part of speech, entities and other features using context, sometimes all you need to a lookups table.  This is a dictionary that you can search and retrieve the information you need. Simple.  

In Cadet, we have three types of lookups.  You can add part of speech, lemmata, and entities.  Each has its own json file that is loaded when your language object is intialized. 

To get comfortable with how spaCy handles lookups, let's work from their [documentation](https://spacy.io/api/lookups#tables).  Lookups are just an object that can be imported.  You can add new tables to the lookups 

```python 

from spacy.lookups import Lookups

lookups = Lookups()
lookups.add_table('pos')

pos_table = lookups.get_table('pos')
pos_table.set("be", "VERB")
assert pos_table['be'] == "VERB"
```
The code above adds a single value to the lookups.  More often, you'll bulk update with a full dictionary of lookups. 

```python 
data = {'lemma_lookup':'path/to/lookup.json','pos_lookup':'path/to/lookup.json','ner_lookup':'/path/to/lookup.json'}

lookups = Lookups()

for table in data.keys():
    language_data = srsly.read_json(data[table])
    lookups.add_table(table, language_data)
```

This is great of one-time updates to the lookups, but we're in the buisness of creating new language models.  How can we add a lookup table to a new language? 

```python
@spacy.registry.lookups("new")
def get_lookups():
    return {"lookups_table_name":"path/to/file.json"}
```

```python
from spacy.pipeline import Lemmatizer 

l = Lemmatizer(nlp.vocab, None)

```