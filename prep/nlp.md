NLP and spaCy
=======================

## NLP

Natural language processing (NLP) is a field of artificial intelligence that allows machines to process and reason about human language using information about the linguistic attributes of texts. Using morphological, semantic, and other features of language, machines can complete a variety of complex tasks, including parsing a text into parts, tagging the linguistic attributes of those parts, entity recognition, sentiment analysis, text categorization, co-reference resolution, topic modeling and [more](https://medium.com/@miranthaj/25-nlp-tasks-at-a-glance-52e3fdff32e2). A common use of NLP is to transform unstructured text into structured data.  For example, the [BookNLP project](https://github.com/dbamman/book-nlp) can process an entire novel and return an exact list of all the unique characters in the text, their genders, how often they speak, and to whom. For another example, see this tutorial ["Holy NLP! Understanding Part of Speech Tags, Dependency Parsing, and Named Entity Recognition"](https://pmbaumgartner.github.io/blog/holy-nlp/).     

## spaCy 

spaCy is an open-source NLP library for Python designed for quick experimentation and applied NLP tasks.  This focus on applied tasks is the most significant difference between spaCy and NLTK, which is designed to be a teaching and research tool. The shift of focus from NLP research to applied NLP has several important outcomes.  

First, the goal of a spaCy model is not state-of-the-art performance (SOTA). spaCy's developers, Matthew Honnibal and Ines Montani, will frequently favor speed, memory usage, and practicality over small gains in accuracy. The goal is a practical, opinionated tool that delivers results in production.  As a result, spaCy offers a library that works well on laptops and consumer devices. It works efficiently on a CPU and does not require GPUs. For our methods to be accessible, we cannot require research computing resources. Whenever possible, we tailor our exercises and tasks to perform on a standard laptop or Colab notebook.  spaCy is also a very extensible library designed for the addition of new pipeline components and custom attributes.  

Additionally, spaCy offers several useful command-line tools for language model training. There is a debug data command that will validate and inspect training data.  The debug tool offers users some bearing on gaps in the data and how the model is likely to perform given the current data. There is a train command that loads a base spaCy language object and then either creates or updates a statistical language model using the data provided.  While it is possible to add and train individual pipelines, this offers a simple CLI for users to create an initial language model from data with parser, tagger, and ner pipelines from the CoNLL-U data.  

##  Further Reading

- Ines Montani has a wonderful free online course to learn spaCy at [course.spacy.io](https://course.spacy.io)
- There's also [spaCy 101](https://spacy.io/usage/spacy-101)

