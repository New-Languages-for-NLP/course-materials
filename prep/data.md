Data Formats
=======================

## JSON  (JavaScript Object Notation)

The vast majority of our data will be in the JSON format. This format begins and ends with curly braces `{}`. Within the braces, we add pairs of keys and values. The key is contained within double quotes and is separated from the value by a colon. For example, `{"key":"value"}`. We can add more "key":value pairs by separating them with a comma.  For example, `{"first_name":"Valentina","last_name":"Tereshkova"}` You can add as many "key":value pairs as you like.     

The most common place you'll find JSON data is in lookups tables.  We use these tables to look up information about a word. We'll use them with part of speech, lemmata and entity lookups.  In that context, the key is the term that we're searching for and the value is the result. For example, `{"be":"VERB"}` or `{"bee":"NOUN"}`. We can store thousands of "key":value pairs in a file.

For more information on JSON, we recommend the [W3 Schools](https://www.w3schools.com/js/js_json_intro.asp) and this [json formatter](https://jsonformatter.curiousconcept.com/).


### Debugging and Validating JSON


Working with JSON can be tricky, especially when you are have large files and you do not know exactly where the error occurs. An open source web application called **[JSONLint](https://jsonlint.com/)** can come handy in this regard. It is designed to help users to debug and validate their JSON files.

To use JSONLint, simply copy your JSON code to the editor and click **Validate JSON**. For example, when the following code  

```json
{
	"be": "VERB"
	"bee": "NOUN"
}

```

is copied to JSONLint and validated, we see this error.

```json
Error: Parse error on line 2:
{	"be": "VERB"	"bee": "NOUN"}
---------------^
Expecting 'EOF', '}', ':', ',', ']', got 'STRING'

```

As it states, the error occurs near the word **"VERB"** and the editor was expecting one of these characters: '}', ':', ',', ']' but received a string. If you have figured it out, we were missing a comma (,) in line 2. When the comma issue is fixed in this example, JSON should validate successfully and you should see a **"Valid JSON"** message in JSONLint.

```json
{
	"be": "VERB",
	"bee": "NOUN"
}

```

From the JSONLint website, here are some rules to consider to ensure your JSON is properly formatted:

* Data is in name/value pairs
* Data is separated by commas
* Objects are encapsulated within the opening and closing curly brackets
* An empty object can be represented by {}
* Arrays are encapsulated within opening and closing square brackets
* An empty array can be represented by []
* A member is represented by a key-value pair, contained in double quotes
* Each member should have a unique key within an object structure
* The value of a member must be contained in double quotes, if it's a string
* Boolean values are represented using the true or false literals in lower case
* Number values are represented using double-precision floating-point format and shouldn't have leading zeroes
* "Offensive" characters in a string need to be escaped using the backslash character \
* Null values are represented by the null literal in lower case
* Dates, and similar object types, aren't adequately supported and should be converted to strings
* Each member of an object or array value must be followed by a comma, except for the last one
* The standard extension for the JSON file is '.json'
* The mime type for JSON files is 'application/json'



## Tabular Data (CSV and TSV)

If you've used a spreadsheet program like Excel or Google Sheets, then you're familiar with tabular data. This is structured information that has rows and columns. To store tabular data in a simple format, programmers often use comma-separated value files. These are simple text files with symbols that split the text into rows and columns. Rows are separated by the new line character `\n`. The row is split into columns by commas. For example, 

`first_name,last_name\nValentina,Tereshkova`

becomes  

| first_name | last_name  |
|------------|------------|
| Valentina  | Tereshkova |


However, we don't have to use commas to separate the columns.  What if you have commas in your data!? To address this problem, it is also common to use tab-separated values using the tab `\t` escape character.  In this project, we'll use two types of tab-separated value formats.  One is the [Stanford CoreNLP format](https://nlp.stanford.edu/nlp/javadoc/javanlp/edu/stanford/nlp/pipeline/CoNLLOutputter.html). We'll use this to move tokenized and annotated text from Cadet to INCEpTION.  Second is the Universal Dependencies, [CoNLL-U](https://universaldependencies.org/format.html) format.  We'll export your annotated texts from INCEpTION using this format because it's a widely adopted format for language model training.  Because the columns are standardized, you won't see a header row in the file.
