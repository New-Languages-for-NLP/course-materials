Data Formats
=======================

## JSON  (JavaScript Object Notation)

The vast majority of our data will be in the JSON format. This format begins and ends with curly braces `{}`. Within the braces, we add pairs of keys and values. The key is contained within double quotes and is separated from the value by a colon. For example, `{"key":"value"}`. We can add more "key":value pairs by separating them with a comma.  For example, `{"first_name":"Valentina","last_name":"Tereshkova"}` You can add as many "key":value pairs as you like.     

The most common place you'll find JSON data is in lookups tables.  We use these tables to look up information about a word. We'll use them with part of speech, lemmata and entity lookups.  In that context, the key is the term that we're searching for and the value is the result. For example, `{"be":"VERB"}` or `{"bee":"NOUN"}`. We can store thousands of "key":value pairs in a file.

For more information on JSON, we recommend the [W3 Schools](https://www.w3schools.com/js/js_json_intro.asp) and this [json formatter](https://jsonformatter.curiousconcept.com/).


## Tabular Data 

If you've used a spreadsheet program like Excel or Google Sheets, then you're familiar with tabular data. This is structured information that has rows and columns. To store tabular data in a simple format, programmers often use comma-separated value files. These are simple text files with symbols that split the text into rows and columns. Rows are separated by the new line character `\n`. The row is split into columns by commas. For example, 

`first_name,last_name\nValentina,Tereshkova`

becomes  

| first_name | last_name  |
|------------|------------|
| Valentina  | Tereshkova |


However, we don't have to use commas to separate the columns.  What if you have commas in your data!? To address this problem, it is also common to use tab-separated values using the tab `\t` escape character.  In this project, we'll use two types of tab-separated value formats.  One is the [Stanford CoreNLP format](https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/pipeline/CoNLLOutputter.html). We'll use this to move tokenized and annotated text from Cadet to INCEpTION.  Second is the Universal Dependencies, [CoNLL-U](https://universaldependencies.org/format.html) format.  We'll export your annotated texts from INCEpTION using this format because it's a widely adopted format for language model training.  Because the columns are standardized, you won't see a header row in the file.
