Data Formats
=======================

## JSON  (JavaScript Object Notation)

The vast majority of our data will be in the JSON format. This format begins and ends with curly braces `{}`. Within the braces, we add pairs of keys and values. The key is contained within double quotes and is separated from the value by a colon. For example, `{"key":"value"}`. We can add more "key":value pairs by separating them with a comma.  For example, `{"first_name":"Valentina","last_name":"Tereshkova"}` You can add as many "key":value pairs as you like.     

The most common place you'll find JSON data is in lookups tables.  We use these tables to look up information about a word. We'll use them with part of speech, lemmata and entity lookups.  In that context, the key is the term that we're searching for and the value is the result. For example, `{"be":"VERB"}` or `{"bee":"NOUN"}`. We can store thousands of "key":value pairs in a file.

For more information on JSON, we recommend the [W3 Schools](https://www.w3schools.com/js/js_json_intro.asp) and this [json formatter](https://jsonformatter.curiousconcept.com/).


## Tabular Data 

If you've used a spreadsheet program like Excel or Google Sheets, then you're familiar with tabular data. This is structured information that has rows and columns. To store tabular data in a simple format, programmers often use comma-separated value files. These are simple text files with symbols that split the text into rows and columns. Rows are separated by the new line charachter `\n`. The row is then split into columns by splitting on the commas. For example, 

`first_name,last_name\nValentina,Tereshkova`

becomes  

| first_name | last_name  |
|------------|------------|
| Valentina  | Tereshkova |




CSV/TSV CoNLL CoNLL-u