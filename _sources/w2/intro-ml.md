Introduction to Machine Learning
=======================

<iframe width="560" height="315" src="https://www.youtube.com/embed/yoU8WGyNLEY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Key ideas from the video 

## Training
The [model](https://docs.paperspace.com/machine-learning/wiki/machine-learning-models-explained#what-is-a-model) is only updated during training and then its "memory" is fixed to provide consistent predictions. 

## Learning 
The model learns to improve its predictions given feedback from the training data.  When incorrect, the [weights and biases](https://docs.paperspace.com/machine-learning/wiki/weights-and-biases) in the model are adjusted deliberately to reduce error. With spaCy, training continues until the model is no longer improving its predictions. 

## Classification Metrics
- [Accuracy and loss](https://docs.paperspace.com/machine-learning/wiki/accuracy-and-loss). As the model trains, the loss (a measure of incorrect predictions) should decrease, while accuracy (percentage of correct predictions) should increase. 

![](https://static.packt-cdn.com/products/9781838555078/graphics/C13314_06_05.jpg)


- True positives (TP): The prediction was yes, and the true value is yes
- False positives (FP): The prediction was yes, but the true value was no
- False negatives (FN): The prediction was no, but the true value is yes

- Precision is a measure of how often the model's predictions were correct. It is the number of correct predictions divided by the total number of predictions made by the model: `TP/(TP+FP)`  
- Recall is a similar measure, but uses false negatives `TP/(TP+FN)`  
- F1 score, the weighted average of precision and recall
- [short video: Precision vs Recall](https://youtu.be/qWfzIYCvBqo)
- [more here](https://docs.paperspace.com/machine-learning/wiki/confusion-matrix)


## [Underfitting and overfitting](https://docs.paperspace.com/machine-learning/wiki/overfitting-vs-underfitting)
- Underfitting describes a model that isn't learning how to make good predictions on your data.  It may need more data, better data, more training, better feature engineering or model architecture.    
- Overfitting describes a model that performs very well with the training data but is unable to make good predictions with new or unseen data. 

## Data splits
[Training, validation and test](https://cs230.stanford.edu/blog/split/) data.  
Training and validation are used during training.  The validation set is checked to measure if the model is improving.  The test set is needed to evaluate the model after training.  It's data that the model has never seen, so it's a good measure of its ability to reason about new data.

## Label distribution 
When we run [spacy debug data](https://spacy.io/api/cli#debug-data) you'll be able to identify labels in your dataset with a small number of examples.  In such a case, we need to be careful that a sufficient  number of examples are present in the training, validation, and test sets.

## Embeddings 
A [word or token embedding](https://en.wikipedia.org/wiki/Word_embedding) is a numerical representation of a word or token. You may also hear them referred to as vectors. A vector is a one dimensional array such as `[0,0,0,0,1]`.


## Further reading
- [Introduction to Precision, Recall and F1](https://youtu.be/jJ7ff7Gcq34)
- [Google machine learning glossary](https://developers.google.com/machine-learning/glossary)