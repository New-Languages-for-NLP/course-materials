Institute Glossary
=======================

Below you will find brief definition of some terms used frequently. If you didn't find what you were looking for, please [contact the tech team](https://newlanguagesfornlp.slack.com/archives/C019617THFF) or add to [this list](https://docs.google.com/document/d/1znbQVzi0Tgb_aFDi6_GYg_a5xUw5mCqGaH6TexFwFG8/edit).


## Technical terms
* **Statistical Language Model (Machine Learning Model)**: An approach to NLP by providing lots of annotated text to the machine which then makes a prediction of a text that it has never seen before.
For more details, refer to [this video](https://youtu.be/OiK2Z2KawnY?t=353). 

* **Rule-based system**: An approach to NLP using formal grammatical rules. For more details, refer to [this video](https://youtu.be/OiK2Z2KawnY?t=188).

 This [medium article](https://medium.com/friendly-data/machine-learning-vs-rule-based-systems-in-nlp-5476de53c3b8) also has a good explanation on Rule-based system and Statistical system.
 
* **Annotations**: Tags or labels on a token based on the role it plays in the text. For example, in the sentence *He eats pizza.*, you might label *eats* as verb and *pizza* as a noun. You have just made annotations for Part of Speech (POS) Layer.

* **Transformers vs Sequence Model (RNN)**: Simply put, Recurrent Neural Networks (RNN) process data in a sequential order, that is, from beginning to end. On the other hand, Transformers uses the attention mechanism to provide context and process the text not necessarily in sequential order. For further details on how transformers work, refer to [this video](https://www.youtube.com/watch?v=iDulhoQ2pro).

* **Transducers**: 


* **Features**: 

* **Entities**: “Real-world” objects, like persons, companies or locations. For example: New York, Haverford College, Google. More explanation on [this video](https://youtu.be/YoUDBUw3D_w?t=1401).


* **Layers**: The types of annotations you can do to text or a token. For example, when you are annotating *He eats pizza.*, in the POS Layer you would annotate *eats* as a "verb" but in the Lemma Layer you would assign *eats* to "eat". Same tokens have different annotations in different layers based on the context.


* **Recommenders**: Enabling Recommenders allow INCEpTION to learn from the annonated data and give suggestions for further annotations. [Read more from the INCEpTION site...](https://inception-project.github.io/releases/0.19.7/docs/user-guide.html#sect_annotation_recommendation)


* **Embeddings**:


* **Transfer Learning**:


* **External recommender**:


## Standard linguistic terms

* **Token**: Meaningful segments that make up the text. For example, the sentence *He eats pizza.* can be said to be made up of four tokens *He*, *eats*, *pizza*, and *. (full stop)* if we were tokenizing based on white spaces. Jump to the [tokenization section of the book](https://new-languages-for-nlp.github.io/course-materials/w1/tokenization.html) or [watch a video from workshop](https://www.youtube.com/watch?v=OiK2Z2KawnY)!

* **Span**: Sequence of one or more tokens. If tokens were only the basis of NLP, it would be difficult to understand some entities that "go together". For example, *New York* collectively refers to a place but if we base our analysis on two separate tokens, we might end up refering to a *York* that is not old! See the use of span in spaCy in [this tutorial](https://youtu.be/THduWAnG97k?t=116).

* **Lemma**: The base (simplest) form or the dictionary form of a token. For example, lemma of *see*, *sees*, *saw*, *seeing*, *seen* would be *see* as all of them are simply different forms of the same word. For explanation, see [this video](https://youtu.be/OiK2Z2KawnY?t=855).

* **POS**: A layer for annotation that assigns part of speech for a token.

* **Morphology**:


* **Agglutination**: 


* **N-gram**:


* **TEI**: Text Encoding Initiative (TEI) is a XML-based encoding of digital texts. More on [this video](https://youtu.be/YoUDBUw3D_w?t=627).
