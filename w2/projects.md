The Project File
=======================

### Introduction

To help organize your work and to create a clear, reproducable and explicit workflow, spaCy offers a feature called "projects." A "project" is a file that acts like a template that runs various steps in your experiment. It's a way to write everything down and clearly establish each step in your model training workflow. In this section, we'll cover the syntax of the project file and its main parts.  We'll then look over the main project file that we have provided you for this workshop, which will read the data from your github repository, prepare the data and then train and package a model for your language. 

> [spaCy projects docs](https://spacy.io/usage/projects)

### Syntax

The `project.yml` file follows a format called yaml which is a simplified and human-friendly form for common data types such as Python lists and dictionaries. If you've ever worked with markdown this should feel somewhat familiar. Marksdown is a simplified format for HTML content. YAML is to data what markdown is for content. In fact, the name means "yet another markup language" (yaml).  

The simplest way to write yaml is to separate a key and value with a semi-colon:
```yaml
first-name: Paula
last-name: "Poundstone"
```
which becomes a Python dictionary
```python
{
  "first-name": "Paula", 
  "last-name": "Poundstone"
}
```

> note that quotes are not required for string values, but can be used if you prefer.

To create a list, use the hyphen `-`.
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

I find it helpful to remember that we're basically building a JSON object. When in doubt, you can fall back on that syntax. Here's a great app to test how your yaml will be converted into data: https://yaml-online-parser.appspot.com/  

There's much more that you can do with yaml, but let's keep it simple for now. We've covered the basics that you'll need for spaCy project files.  

> For more, here's the [awesome yaml page](https://github.com/dreftymac/awesome-yaml)  


### Project file sections

1. Most project files begin with basic **metadata** about the project.  This is often just a title and description, but can include whatever you feel is important to record and give context for the project. 

```yaml
title: "New Language Model using UD Data"
authors: 
  - Sudipta
  - Emma
description: "This project..."
date: 29/12/2021
```

2. The **variables** section lets you clearly declare project settings and variables. These variable can be called and reused within the project using the format `${ vars.your-variable }`. You can also nest variables. We can use the train_file variable from below by calling `${ vars.files.train_file }`.  Using the variables section makes your project more consistent and easier to read. 

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

3. The directories list is a list of project subfolders.  If you want spaCy to always create a new folder for you, just add it to the list.  This is nicer than adding 'mkdir' calls in the scripts sections.

```yaml
directories: ["assets", "assets/conllu", "training", "configs", "corpus", "packages"]
```

> spaCy uses the pathlib library to confirm that each directory exists and creates any that are missing [src](https://github.com/explosion/spaCy/blob/f40e237c5a72784034b61425f7d863ce1ac9f46e/spacy/cli/_util.py#L162)

4. The **assets** section describes the actions to be taken when you call `spacy project assets`. In most cases, this will fetch data from a remote source such as GitHub and download it to the computer currently running the project. The approach means that anyone running the experiment will be using the same data and not something that's specific to their computer. 

For the example below, let's say that `vars.treebank` is Yoruba. The code below will clone the `New-Languages-for-NLP/Yoruba` github repository and save all the files in the `assets/Yoruba` folder. 
```yaml
assets:
  - dest: "assets/${vars.treebank}"
    git:
      repo: "https://github.com/New-Languages-for-NLP/${vars.treebank}"
      branch: "main"
      path: ""

```
> For more sees the [spaCy docs](https://spacy.io/usage/projects#data-assets)

5. The **workflows** section makes it possible to run several commands in sequence.The most most common use of this feature is `spacy project run all`. For example, 

```yaml
workflows:
  all:
    - install
    - convert
```
will run the `install` and then the `convert` commands.  Commands can also be run individually, but the workflow provides a clear sequence in which they are meant to be run.   


6. Probably the most important section of a project.yml file is the **commands** section. This section describes an action or step within the larger workflow. Each action has a `name`. It can also require certain inputs and outputs.  The `deps` section will test that required files are present.  An `outputs` section will confirm that the expected output files were created.  The `script` section works like the command line. You can run several commands in sequence utilizing information from `variables`.  

```yaml
commands:
  - name: split
    help: "Split the data into train, validation, and test"
    script: 
      - "python scripts/split.py ${vars.test_size} ${vars.random_state} ${vars.lang}"
    deps:
      - "corpus/converted"
    outputs:
      - "corpus/train.spacy"
      - "corpus/dev.spacy"
      - "corpus/test.spacy"
```      

### The New Language Project File

...
