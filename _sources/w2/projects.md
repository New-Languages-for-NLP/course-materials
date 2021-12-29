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

Most project files begin with basic **metadata** about the project.  This is often just a title and description, but can include whatever you feel is important to record and give context for the project. 

```yaml
title: "New Language Model using UD Data"
authors: 
  - Sudipta
  - Emma
description: "This project..."
date: 29/12/2021
```

The **variables** section lets you clearly declare project settings and variables. These variable can be called and reused within the project using the format `${vars.your-variable}`. 

```yaml
vars:
  config: "config.cfg"
  name: "ner_fashion"
  version: "0.0.0"
  # Change this variable if you want to use the GPU (gpu_id: 0)
  gpu_id: -1
```

The directories list is a list of project subfolders.  If you want spaCy to always create a new folder for you, just add it to the list.  This is nicer than adding 'mkdir' calls in the scripts sections.

```yaml
directories: ["assets", "assets/conllu", "training", "configs", "corpus", "packages"]
```

> spaCy uses the pathlib library to confirm that each directory exists and creates any that are missing [src](https://github.com/explosion/spaCy/blob/f40e237c5a72784034b61425f7d863ce1ac9f46e/spacy/cli/_util.py#L162)

The **assets** section describes the actions to be taken when you call `spacy project assets`. In most cases, this will fetch data from a remote source such as GitHub and download it to the computer currently running the project. The approach means that anyone running the experiment will be using the same data and not something that's specific to their computer. 

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

The **workflows** section makes it possible to run several commands in sequence.The most most common use of this feature is `spacy project run all`. For example, 

```yaml
workflows:
  all:
    - install
    - convert
```
will run the `install` and then the `convert` commands.  Commands can also be run individually, but the workflow provides a clear sequence in which they are meant to be run.   


Probably the most important section of a `project.yml` file is the **commands** section. This section describes an action or step within the larger workflow. Each action has a `name`. It can also require certain inputs and outputs.  The `deps` section will test that required files are present.  An `outputs` section will confirm that the expected output files were created.  The `script` section works like the command line. You can run several commands in sequence utilizing information from `variables`.  For example, the code below will run a python script called `split.py` to create files needed for model training. If there is more than one action in a command, you can add as many as you need. 

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


### The New Language Project File

For the New Languages for NLP workshops, we've created a project file for you that can be adapted to meet the specific needs of your project. In this section, we've walk through the various sections and scripts of the project.  We've made some choices on your behalf. They may be right, or you may want to change things. Let's see what's there.   

In your language teams GitHub repository, you'll find a `newlang_project` folder.  
```
newlang_project
│   README.md
│   project.yml    
│
└───scripts
    │   convert.py
    │   split.py
    │   update_config.py
```

Let's start with the **project.yml** file. 

You'll find a **metadata** section that you can update however you like using the yaml format.   

The **vars** section will have some information that is specific to your team.  
    - The `config` setting is the name and location of the config file.  We'll just have `config.cfg` in the project directory, so nothing fancy here. 
    - `lang` is the ISO-style abbreviation for your language. 
    - `treebank` is the name of your language's repository (and is ususally the same as the language name).
    - `test_size` is the percentage of data that you want to set aside for model validation and testing. An 80/20 split is a good place to start, so you'll see it set initially to `0.2`. For more, this [stackoverflow discussion](https://stackoverflow.com/questions/13610074/is-there-a-rule-of-thumb-for-how-to-divide-a-dataset-into-training-and-validatio) is very informative. 
    - We need to evenly distribute your texts between the training and validation datasets. We split each text into blocks of 10 sentences. This is defined by the `n_sents` variable.
    - To ensure that the test and train split is consistent and reproducable, we use a number called `random_state`. More [here](https://scikit-learn.org/stable/glossary.html#term-random_state).
    - The `package_name` is used during packaging and sets the package's metadata name. Basically, what is the name of your language model? 
    - Similarly, `package_version` sets the package metadata for version.
    - spaCy comes with some basic ways to log training data.  However, [Weights and Biases](https://wandb.ai/) provides an excellent way to record, manage and share experiment data. You'll need to create a free account and get an API key to use bandb.  When set to `true` your project will use bandb (we highly recommend). You can change this to `false` if you prefer spaCy defaul logging. 
    - Finally, model training with graphics chips (GPUs) is often faster than with a standard CPU. We recommend using Colab for their free GPUs.  In such a case you'd change `-1` (CPU) to `0` (the GPU id).        

```yaml 
vars:
  config: "config"
  lang: "yi"
  treebank: "yiddish"
  test_size: 0.2
  n_sents: 10
  random_state: 11
  package_name: "Yiddish NewNLP Model May 2022"
  package_version: "0.1"
  wandb: true 
  gpu: -1
```

**Assets** is configured to use your language repo name to fetch project data from GitHub.  It will save all that data in the `assets/your-language-name` folder.   

The **commands** section is the heart of the project file.  Let's take some time to understand each command and what it does. 