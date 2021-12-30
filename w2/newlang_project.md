The New Language Project File
=======================

For our workshops, we've created a project file for you. It can be adapted to meet the specific needs of your project. In this section, we will walk through the various sections and scripts of the project.  We've made some choices on your behalf. They may be right, or you may want to change things. Let's see what's there.   

In your language team's GitHub repository, you'll find a `newlang_project` folder.  
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

- The `config` setting is the name and location of the config file.  We'll just have `config.cfg` in the project directory, so nothing fancy here. 
- `lang` is the ISO-style abbreviation for your language. 
- `treebank` is the name of your language's repository (and is ususally the same as the language name).
- `test_size` is the percentage of data that you want to set aside for model validation and testing. An 80/20 split is a good place to start, so you'll see it set initially to `0.2`. For more, this [stackoverflow discussion](https://stackoverflow.com/questions/13610074/is-there-a-rule-of-thumb-for-how-to-divide-a-dataset-into-training-and-validatio) is very informative. 
- To evenly distribute your texts between the training and validation datasets, we split each text into blocks of 10 sentences. This is defined by the `n_sents` variable.
- To ensure that the test and train split is consistent and reproducible, we use a number called `random_state`. More [here](https://scikit-learn.org/stable/glossary.html#term-random_state).
- The `package_name` is used during packaging. It sets the package's metadata name. Basically, what is the name of your language model? 
- Similarly, `package_version` sets the package metadata for version.
- spaCy comes with some basic ways to log training data.  However, [Weights and Biases](https://wandb.ai/) provides an excellent way to record, manage and share experiment data. You'll need to create a free account and get an API key to use bandb. When set to `true`, your project will use bandb (we highly recommend it). You can change this to `false` if you prefer spaCy's default logging. 
- Finally, model training with graphics chips (GPUs) is often faster than with a standard CPU. We recommend using Colab for their free GPUs.  In such a case, you'd change `-1` (CPU) to `0` (the GPU id).        


**Assets** is configured to use your language repo name to fetch project data from GitHub.  It will save all that data in the `assets/your-language-name` folder.   

The **commands** section is the heart of the project file.  Let's take some time to understand each command and what it does. 

The `install` command will read the files in the `2_new_language_object` directory and will install the customized spaCy language object that you created for your language in Cadet. The language object will tell spaCy how to break your texts into tokens and sentence spans.

`Convert` will fetch your CoNLL-U and CoNLL 2002 (ner) files from the `3_inception_export` folder.  It creates a spaCy Doc object for each text and then splits the Doc into separate documents with 10 sentences each. For each text file, the `convert` script will look for a CoNLL 2002 file with the same name.  If that text exists, it will add the named entity data in the file to the existing Doc objects. It will then save all the Docs to disk using the `.spacy` binary format. 
The outcome is a `.spacy` for each text that includes the tokenization, sents, part of speech, lemma, morphology and named entity data.

The `split` command loads all of the `.spacy` files and creates a list of Doc objects.  We then randomly shuffle them so that different kinds of text are evenly distibuted across the corpus.  Using a [`test_train_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) function, we divide the corpus into a training and validation set. The split is determined by the `test_size` variable. The model will learn how to make accurate predictions using the training data. We then use the validation set to assess how well the model performs on completeley new and unseen data. We want the model to learn general rules and patterns rather than overfitting on one particular set of data. The validation set provides a measure of model improvement as part of the training process. Because the model has seen this data before, it's no longer useful as a tool to evaluate the trained model's performance.  So before we get started training, we also set aside 20% of the validation data to make a test set.  This final set of totally unseen data lets us measure how well the model has learned what we've asked it to learn.

The `config` command is rather dull by comparison.  It creates a generic `config.cfg` file (for more on config files, see the Config section in these course materials).  It updates the `train` and `dev` settings in the config file to point to your new `train.spacy` and `dev.spacy` files from the `split` command.  If you're using Weights and Biases, it will also change the `training logger`. 

The `debug` command runs `spacy debug data`, which provides a good overview of your prepared data.  This can help identify problems that will lead to poor model training. It's a good check-in and moment of reflection on the state of your data before moving forward. For more, see the [spaCy docs](https://spacy.io/api/cli#debug-data). 

The `train` command is the moment we've all been waiting for. Go ahead and press the launch button! 🚀 This step will train the model using the settings in the config file.  

When training begins, you'll see a bunch of numbers. Let's make sense of what they're saying.

You'll see a list of what components are currently being trained.  `Pipeline: ['tok2vec', 'tagger', 'parser', 'ner']` Tok2vec are token embeddings or numerical representations of tokens that can be used efficiently by the model. The tagger will learn to predict part of speech values for your tokens. The parser will learn to predict grammatical structure. The ner component learns to predict named entities in the text. 

For each of these components, spaCy will print training metrics. So let's dive into this pile of forbidding verbiage and numbers.

```
E    #       LOSS TOK2VEC  LOSS TAGGER  LOSS PARSER  LOSS NER  TAG_ACC  DEP_UAS  DEP_LAS  SENTS_F  ENTS_F  ENTS_P  ENTS_R  SCORE 
---  ------  ------------  -----------  -----------  --------  -------  -------  -------  -------  ------  ------  ------  ------
```
- The `E` refers to the epoch. An epoch is one complete pass of all the data through the model. You can set the number of epochs to complete during training or let spaCy optimize the number of epochs automatically (this is the default). 
- Every 200 examples, spaCy outputs accuracy scores in the `#` column. 
- `LOSS` refers to training loss. Loss is a measure of error. During training, the model will try to learn how to improve its predictions. Decreasing loss can suggest that the model is learning and improving.  If the loss value flattens or plateaus, the model has probably stopped learning or reached the best result for a given set of parameters and data.  You will find a loss measure for each of the pipeline components being trained. If the loss varies greatly and looks like a zigzag, the model is struggling to improve its predictions in a deliberate manner. `LOSS TOK2VEC  LOSS TAGGER  LOSS PARSER  LOSS NER`
- `TAG_ACC` refers to the accuracy of the tagger component. [Accuracy](https://developers.google.com/machine-learning/glossary#accuracy) is the number of correct predictions divided by the total number of predictions made.
- `DEP_UAS` and  `DEP_LAS` are the unlabeled attachment score (UAS) and labeled attachment score (LAS) for the dependency parser. This is a measure of how many times the model correctly predicted the correct head.
- `SENTS_F` gives the model's [f-score](https://en.wikipedia.org/wiki/F-score) for sentence prediction.     
- `ENTS_F  ENTS_P  ENTS_R` relate to the model's predictions of named entities. The f-score is the mean of precision and recall.   
- Finally, spaCy logs a `SCORE` for the model's predictions overall. This gives a rough number for the model's overall accuracy.  As a general rule, increasing numbers means that the model is improving. By default, spaCy will end training when the score stops rising. 

The **evaluate** command takes the trained model and tests it with the test data.  Recall that these are examples that the model has never seen, so they provide the best measure of its performance. The output will be saved as a json file in the metrics folder.
      
Finally, the **package** command saves your trained model in a single tar file that can be shared and installed on other computers.  

Keep in mind that you'll need some persistence and patience along the way. You'll probably need to run multiple experiments before you find the right blend of data and parameters to create a final product.  The instructors are happy to help along the way and we look forward to learning together with you. When all commands are successfully run, you will have converted your text annotations from inception and language object from Cadet into a trained statistical language model that can be loaded with spaCy for a large variety of research tasks.    