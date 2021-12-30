The Project File
=======================

### Introduction

To help organize your work and to create a clear, reproducable and explicit workflow, spaCy offers a feature called "projects." A "project" is a file that acts like a template that runs various steps in your experiment. It's a way to write everything down and clearly establish each step in your model training workflow. In this section, we'll cover the syntax of the project file and its main parts.  

> More here: [spaCy projects docs](https://spacy.io/usage/projects)

### Syntax

The `project.yml` file follows a format called yaml ("yet another markup language"), which is a simplified and human-friendly form for common data types such as Python lists and dictionaries. If you've ever worked with markdown, this should feel somewhat familiar. Marksdown is a simplified format for HTML content. YAML is to data what markdown is to content. 

The simplest way to write yaml is to separate a key and value with a semi-colon:
```yaml
first-name: Paula
last-name: "Sloane"
```
which becomes a Python dictionary
```python
{
  "first-name": "Paula", 
  "last-name": "Sloane"
}
```

> Note that quotes are not required for string values, but can be used if you prefer.

To create a list, use the hyphen `-`.
```yaml
- Fred
- Inna
- Oleh 
```
```python 
['Fred', 'Inna', 'Oleh']
```

These two basic forms can be combined to create complex objects. For example, let's make up a dictionary of guests and what they're bringing to a party. Note that indentation (two spaces) is used to create values that are themselves dictionaries or lists (called nesting).   
```yaml
guests:
  - name: Inna
    bringing:
      - tacos
      - ice cream
      - napkins
  - name: Oleh
    bringing:
      - pickles
      - hoagies  
```
```python
{
    "guests": [
        {"name": "Inna", "bringing": ["tacos", "ice cream", "napkins"]},
        {"name": "Oleh", "bringing": ["pickles", "hoagies"]},
    ]
}
```

I find it helpful to remember that we're basically building a [JSON object](https://new-languages-for-nlp.github.io/course-materials/prep/data.html). When in doubt, you can fall back on that syntax. Here's a great app to test how your yaml will be converted into data: https://yaml-online-parser.appspot.com/  

There's much more that you can do with yaml, but let's keep it simple for now. We've covered the basics that you'll need for spaCy project files.  

> For more, here's the [awesome yaml page](https://github.com/dreftymac/awesome-yaml)  


### Project file sections

Most project files begin with basic **metadata** about the project.  This is often just a title and description, but it can include whatever details you feel are important to give give context for the project. For example:

```yaml
title: "New Language Model using UD Data"
authors: 
  - Sudeepta
  - Emma
description: "This project loads data from the Abyssinian UD treebank and trains a language model with a tagger and parser."
date: 29/12/2021
```

The **variables** section lets you clearly declare project settings and variables. These variables can be called and reused within the project using the format `${vars.your-variable}`. 

```yaml
vars:
  config: "config.cfg"
  name: "ner_fashion"
  version: "0.0.0"
  # Change this variable if you want to use the GPU (gpu_id: 0)
  gpu_id: -1
```

The directories list is a list of project subfolders.  If you want spaCy to create a new folder for you, just add it to the list.  

```yaml
directories: ["assets", "assets/conllu", "training", "configs", "corpus", "packages"]
```


The **assets** section describes the actions to be taken when you call `spacy project assets`. In most cases, this will fetch data from a remote source such as GitHub and download it to the computer currently running the project. This action ensures that anyone running the experiment will be using the same data and not something that's specific to their computer. 

For the example below, let's say that `vars.treebank` is Yoruba. The code below will clone the `New-Languages-for-NLP/Yoruba` github repository and save all the files in the `assets/Yoruba` folder. 
```yaml
assets:
  - dest: "assets/${vars.treebank}"
    git:
      repo: "https://github.com/New-Languages-for-NLP/${vars.treebank}"
      branch: "main"
      path: ""

```
> For more, see the [spaCy docs](https://spacy.io/usage/projects#data-assets)  

The **workflows** section makes it possible to run several commands in sequence. The most common use of this feature is `spacy project run all`. For example, 

```yaml
workflows:
  all:
    - install
    - convert
```
will run two commands: first, the `install` command, then the `convert` command.  Commands can also be run individually, but the workflow provides a clear sequence in which they are meant to be run.   


Probably the most important section of a `project.yml` file is the **commands** section. This section describes an action or step within the larger workflow. Each action has a `name`. It can also require certain inputs and outputs.  The `deps` section will test that required files are present.  An `outputs` section will confirm that the expected output files were created.  The `script` section works like the command line. You can run several commands in sequence. You can use variables from the `variables` section.  For example, the code below will run a python script called `split.py` to create files needed for model training with the `test_size`, `random_state` and `lang` variables. If there is more than one action in a command, you can add as many as you need. 

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

> There's much more to spaCy projects, but this outline should give you the essentials to understand how the file is formatted and what it does. 
