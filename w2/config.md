The Config File
=======================

For these workshops you will likely not need to make any changes to the `config.cfg` file. This section is here for participants who want a basic understanding of what the config file does. Advanced users who are interested in changing model components and architecture are best served by the existing spaCy documentation on the config system.    

### The Basics

The `config.cfg` file is similar in many ways to the `project.yml` file. It offers a stable place to record your model's parameters and settings.  

- It has an `[nlp]` section that contains settings for the NLP object. If you don't have any named entity data, you may want to edit this line: `pipeline = ["tok2vec","tagger","parser","ner"]` to remove `"ner"`.
 
- There is a `[components]` section with settings for each individual component in the pipeline.  This section is especially useful for custom components and for deviating from spaCy default configurations. 
- The `[training]` section contains various hypterparameters that can be changed, such as seed, dropout, and evaluation frequency. 

### Customizing Pipeline Training 

The section in the documentation on [Defining pipeline components](https://spacy.io/usage/training#config-components) may be especially helpful for teams that are interested in customizing the organization and capabilities of their model.  

For example, what if you want to fine-tune an existing tokenizer rather than training from scratch?  Perhaps fine-tuning from an existing multi-lingual model would be better than training on a small set of annotated texts? 

```yaml
[nlp.tokenizer]
source = "xx_ent_wiki_sm"
```
Adding the code above to your `config.cfg` file instructs spaCy to load the tokenizer from the small multilingual model and then fine-tune it using your training data.  #TODO would this actually work for tokenizer, or just for components?


For more in-depth and practical information, please see the spaCy documentation:
- [Useage](https://spacy.io/usage/training#config)
- [API](https://spacy.io/api/data-formats#config)

