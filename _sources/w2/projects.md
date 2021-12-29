The Project File
=======================

### Introduction

To help organize your work and to create a clear and explicit workflow, spaCy offers a feature called "projects." A "project" is a file that acts like a template and script that runs various steps in your experiment. It's a way to write everything down and clearly establish each step in your workflow. In this section, we'll cover the syntax of the project file and its main parts.  We'll then look over the main project file that we have provided you for this workshop, which will read the data in your github repository, prepare the data and then train and package a model for your language. 

> [spaCy Projects docs](https://spacy.io/usage/projects)

### Syntax

The `project.yml` file follows a format called yaml which is a simplified and human-friendly form for common data types such as Python lists and dictionaries. If you've ever worked with markdown, that is a simplified format for HTML content.YAML is to data what markdown is for content.  

The simplest way to write yaml is to separate a key and value with a semi-colon:
```yaml
name: Fred
```
Becomes a Python dictionary
```python
{'name': 'Fred'}
```

Or to create a list, use the hyphen `-`
```yaml
- Fred
- Inna
- Oleh 
```
```python 
['Fred', 'Inna', 'Oleh']
```

These two basic forms can be combined to create complex objects. For example, let's make a dictionary of guests and what they're bringing to the party. Note that indentation (two spaces) is used to create values that are themselves dictionaries or lists (called nesting).   
```yaml
guests:
  - name: Inna
    bringing:
      - tacos
      - ice
      - napkins
  - name: Oleh
    bringing:
      - dip
      - hoagies  
```
```python
{
    "guests": [
        {"name": "Inna", "bringing": ["Tacos", "Ice", "Napkins"]},
        {"name": "Oleh", "bringing": ["Dip", "Hoagies"]},
    ]
}
```

There's much more that you can do with yaml, but this should be the basics that you'll need to understand a spaCy project file.  

> For more here's the [awesome yaml page](https://github.com/dreftymac/awesome-yaml)  

> Here's a great app to test how your yaml will be converted into data: https://yaml-online-parser.appspot.com/


### Project file sections

1. Most project files begin with basic metadata about the project.  This is often a title and description.

```yaml
title: "New Language Model using UD Data"
authors: 
  - Phil 
  - Emma
  - Sudipta
description: "This project...
```

2. The variables section lets you clearly declare project settings and variables. These variable can be called and reused with the format `${ vars.your-variable}` You can also nest variables. We can use the train_file variable below by calling `${ vars.files.train_file }`.  Using the variables section makes your project more consistent and easier to read. 

```yaml
vars:
  config: "config.cfg"
  name: "ner_fashion"
  version: "0.0.0"
  # Change this variable if you want to use the GPU (gpu_id: 0)
  gpu_id: -1

  files:
    train_file: "fashion_brands_training.jsonl"
    eval_file: "fashion_brands_eval.jsonl"

  prodigy:
    train_dataset: "fashion_brands_training"
    eval_dataset: "fashion_brands_eval"
```

3. The directories list is a list of project subfolders.  If you want spaCy to always create a new folder for you, just add it to the list.  This is cleaner than adding 'mkdir' calls in the scripts sections.
 
```yaml
directories: ["assets", "training", "configs", "corpus", "packages"]
```
### The New Language Project File

...
