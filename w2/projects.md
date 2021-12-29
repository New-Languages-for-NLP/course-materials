The Project File
=======================

### Introduction

To help organize your work and to create a clear and explicit workflow, spaCy offers what they call "projects." A "project" is a file that acts like a script to run various steps in your experiment. It's a way to write everything down and explain the steps of your work. In this section, we'll cover the syntax of the project file and its main parts.  We'll then look over the main project file that we have provided you for this workshop, which will read the data in your github repository, pre-process the data and then train and package a model for your language. 

> [spaCy Projects docs](https://spacy.io/usage/projects)

### Syntax

The `project.yml` file follows a format called yaml which is a simplified and human-friendly form for common data types such as Python lists and dictionaries. If you've ever worked with markdown, that's a simplified format for HTML content.YAML is to data what markdown is for content.  

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

There's much more that you can do with yaml, but we've cover the basics that you'll need to understand a spaCy project file.  

> For more here's the [awesome yaml page](https://github.com/dreftymac/awesome-yaml)
> Here's a great app to test how your yaml will be converted into data: https://yaml-online-parser.appspot.com/


### Project file sections

...


### The New Language Project File

...
