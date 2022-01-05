Using Colab
=======================

For these workshops, we have chosen to use a free service offered by Google called Colab.  Colab is an environment for running code notebooks using Google's infrastructure on the cloud.  It allows us to all work in our browsers in the same environment with similar computational power and memory.  It doesn't matter if you're running Windows, or Mac or Linux.  Remarkably, Google also provides free usage of graphics processing chips (GPUs), which are much faster for model training.  To improve your experience, We have purchased a Colab Pro subscription for each team.  With this subscription you will have access to greater processing and memory sources and you will not be subject to time limitations as well. 


---

### Colab 101

When using Colab to train your spaCy model, there are a few things to know and keep in mind.


If you've used Jupyter Notebooks before, then Colab should feel very familiar.  Colab runs on Jupyter, so any existing notebooks you have will work.  

One key difference is that you need a Google account to log in to Colab. 

Colab is similar to Google Docs and is part of Google Drive. You can open and run a shared Colab, but you may not have permission to change it.  With File > Save a copy in drive, you can create your own copy that can be changed and saved however you like. 


### Runtime 

Another important difference is the runtime.  When you run a Jupyter notebook on your laptop or desktop computer it connects to a runtime or kernel on your computer.  The runtime is basically the environment  where you scripts are run and processed. Jupyter displays the notebook, but the runtime does the actual work of running your code. 

One of the key design choices behind Colab is that everyone starts with the same runtime environment  running Ubuntu 18 with Python 3.7 and a host of common machine learning and data science libraries already installed. This generic kernel means that you can connect, run your code and get things done. 
- If your computer falls asleep or you close your browser, Colab will timeout after 90 minutes.  If you leave the browser open, it will keep a session open for as much as 12 hours. However, in my experience these numbers aren't set in stone and Colab can be finicky.  I find it helpful to keep the Colab tab open while I work some other task on the computer. It's like a pet you have to keep an eye on.  
- If your connection drops out, you can use the reconnect button to rejoin your session if it's still running.  Often times, the notebook is still chugging along and you'll be right back where you need to be. If the runtime has timed out, reconnect will connect you with a new generic runtime and you'll need to start over.  

Any files that you've created in a session can be lost. spaCy's project system will keep up safe most of the time.  However, once your model is trained, don't forget to run the cells to package it and download the file to your local machine.  You can then save it in GitHub. 

> One trick that you can try is to limit the number of training epochs.  In your `config.cfg` file, find the `[training]` section and change `max_epochs = 0` to a number that works for you, such as `10`.

> If you need to hard reset your notebook and just start from scratch, use Runtime > Factory reset runtime.  


### CPUs and GPUs

As mentioned before, one of the benefits of Colab is the use of GPUs.  If you know someone that's really into computer games or crypto mining, then you may have seen one hooked up to a liquid cooling system with neon lights.

In a nutshell, GPUs are great for machine learning because they allow for lots of parallel or concurrent processing. Most CPUs nowadays have between 2 and 6 cores.  That means that the computer can only process two to six tasks at a time. For those of you thinking "ah ha, what about multithreading," let's just leave that aside for the moment. GPUs have thousands of cores and can run thousands of computations simultaneously. They have lower precision, so they're not good for all tasks, but they're just the thing for the matrix multiplication that drives much of machine learning today.  

- Your Colab notebook should already have GPUs enabled. If it does not, just go to Edit > Notebook Settings and select GPU under hardware accelerator.  
- By default, your `project.yml` will show `gpu: 0` in the `vars` section.  This tells Colab to use the first GPU with id 0.  If you need to use the CPU, you can change this to `-1`.


### Table of Contents 

On the left hand side of the page, you'll find a menu for the table of contents, find and replace, and Files among others. 

- The table of contents gives you a good way to view the larger structure of the notebook and its main parts.  If you want to jump to a specific section of the notebook, the toc is great for that. 
- The Files section here is also very useful.  It lets you view the files on the current system.  You can also double-click on the files to edit them.  This is very useful if you want to make small changes to your `config.cfg` or `project.yml` files. Note that any changes to files will not be shown until you click on Refresh (the folder with a circle).


### Cell input

If you are using Weights and Biases for logging, you will be asked if you want to use an existing account and for you API key.  Colab does a good job of handling input. Just click next to the area requesting input and you should see a small blue box that you can type in.  Enter your information and press Enter. 


Links and further reading: 
- https://colab.research.google.com/
- [Getting Started With Google Colab](https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c)