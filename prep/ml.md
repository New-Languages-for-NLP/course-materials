Neural Networks and Machine Learning
=======================

Neural networks have become an essential method of Machine Learning since the first “perceptron” was invented in 1958. A neural network is a graph composed of nodes and edges that are typically structured as layers in their most basic form. During inference, information flows, layer by layer, in one direction making for a directed graph (DAG). There are different types of layers, for example, fully connected or convolutional, that characterize the connections between layers. Each connecting edge has a weight value that can be adjusted. By deliberately improving these weights, the network can either emphasize or discard specific inputs. Additionally, before passing the weighted inputs forward to the next node, a non-linear activation function is applied.

<iframe width="560" height="315" src="https://www.youtube.com/embed/UOvPeC8WOt8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>  

![](https://miro.medium.com/max/645/0*LJBO8UbtzK_SKMog)

In the late 1980s, it became possible to "backpropagate" and update the weights based on the error in the model's predictions. Together with gradient descent, backpropagation enabled models to automatically improve their predictions without handwritten rules and criteria.  

[Code intro to backprop and layer chaining](https://thinc.ai/docs/concept)

As the computations could be parallelized on GPUs and more data became available, it has sparked a period of rapid innovation and heightened expectations. Many-layered networks with increasingly complex architectures can complete computer vision and natural language tasks with near- or super-human precision.

![](https://miro.medium.com/max/3840/1*5K-1CSOB2mb5Jn2L8K3f9Q.gif)

As models become more complex, they require more processing power, training time, and memory. In addition to the exciting new potential and new capabilities of machine learning, scholars are also beginning to evaluate the environmental and social costs of models built in person-years using petabytes of data ([1](https://faculty.washington.edu/ebender/papers/Stochastic_Parrots.pdf),[2](https://arxiv.org/pdf/1906.02243.pdf)).   

## Further Reading

- Andrew Trask, [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning)
- Ian Goodfellow et al., [Deep Learning](https://www.deeplearningbook.org/)