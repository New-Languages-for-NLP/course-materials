Python 
=======================

Creating, training, and using spaCy natural language processing (NLP) models requires code in the Python programming language. For this workshop, we don't expect that you'll be comfortable writing that code on your own. We've tried to put together tools with user interfaces that you can use instead of writing Python code. These tools are experimental, and they might not work in all situations. As a backup, we've prepared Jupyter notebooks where you can access the Python code directly.

Jupyter notebooks provide an environment for reading, writing, and running code in a number of languages, including Python. What sets them apart from other environments is that they make it easy to juxtapose (even lengthy) explanations in human-readable text and images along with the code. You can read more [about Jupyter Notebooks in theory and practice on Programming Historian](https://programminghistorian.org/en/lessons/jupyter-notebooks). The notebooks we prepare will explain every step, along with what parameters you need to change, depending on what you're trying to do. If there's something you don't understand in our notebooks, please ask! We'll be improving them based on your feedback. If something isn't clear to you (regardless of your technical background), we need to do a better job explaining it.

No prior experience with Python is needed for this workshop, but there's a few things you should keep in mind:

* Python (like any other programming language) is very particular about syntax. Very often, when code doesn't run correctly, it's because there's a misplaced parenthesis, quotation mark, extra space, or something else small.
* Python, specifically, is very fussy about whitespace and indentation. Things need to be indented correctly (using tabs) to work. Be very careful if you ever add or delete any indentation.
* With spaCy, the text that you process using one of the spaCy models is contained in a doc object that contains a lot of properties and other objects (which also have properties). Even if you're not familiar with how objects work in Python, we'll have lots of examples for how to access the things that interest you.
* A lot of Python comes down to learning how to debug the error messages you run into. Feel free to post your error messages on Slack (along with a link to the notebook and data set where it's occurring), and we can try to help! A few tips...
    * "Object is not callable": don't use the curvy parentheses
    * "Object is not subscriptable": don't use the square parentheses
    * "Invalid syntax": you used the wrong number of equals signs, or maybe the actual error is multiple lines up
    * "Name error": that doesn't exist yet, or you spelled it wrong
*  If you want some exposure to Python basics, check out these Programming Historian tutorials:
    * [Working with text files in Python](https://programminghistorian.org/en/lessons/working-with-text-files)
    * [Manipulating strings in Python](https://programminghistorian.org/en/lessons/manipulating-strings-in-python)
    * [Counting word frequencies in Python](https://programminghistorian.org/en/lessons/counting-frequencies)
* You're likely  to  hear a lot of new  terms and concepts. It's always good to Google  things that are new. In nearly every case others have asked the same questions before and there's a question-answering community called Stack Overflow that has voted for the best answers. Stack Overflow answers typically come up near the top of Google search results, and are worth checking out.