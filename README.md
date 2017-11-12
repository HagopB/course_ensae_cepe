# course - Deep Learning
### What is this repository for? 
Notebooks and support necessary for the "Deep Learning" course. During the course, we'll apply together the studied notions (MLP, CNN, , Transfer Learning, RNN) on three practical cases: Mnist handwritten digit recognizer, cats vs dogs and IMDB critics. The solutions ([MNIST](https://github.com/HagopB/course_ensae_cepe/blob/master/notebooks/MNIST_CNN.ipynb), [Cats vs Dogs](https://github.com/HagopB/course_ensae_cepe/blob/master/notebooks/CATS_vs_DOGS.ipynb) & [IMDB](https://github.com/HagopB/course_ensae_cepe/blob/master/notebooks/IMDB_CRITICS.ipynb))are presented in the "./notebooks" folder. At the end of the course, you'll be asked to design and train your own model to solve an image recognition competition on kaggle [The Nature Conservancy Fisheries Monotirong](https://www.kaggle.com/c/the-nature-conservancy-fisheries-monitoring). A potential solution to this case is presented in this repo: [https://github.com/HagopB/fisheries_kaggle](https://github.com/HagopB/fisheries_kaggle).

### How do I get set up ?  
Install Anaconda 3
Import the conda environment named `deepenv` using : 
```
conda env create -f deepenv.yml
```

Activate that environment using :
```
source activate deepenv
```
Now all the dependencies must be installed without problems (Keras 2, tensorflow 1 ...)

### Contents
```
└── 
    ├── data                                # data for the practice cases
         ├── dogscats.zip                   # data for Cats vs Dogs
         └── data_fisheries.zip             # data for fisheries competition
    ├── images                              # utils images
    ├── notebooks                           # data folder contaning notebooks and utils
         ├── MNIST_CNN.ipynb                # notebook for MNIST
         ├── IMDB_CRITICS.ipynb             # notebook for IMDB critics sentiment analysis
         ├── CATS_vs_DOGS.ipynb             # cats vs dogs image classification - using Transfer Learning
         └── utils.py                       # utils necessary for the two notebooks
    ├── ENSAE-ENSAE Cepe - Deep Learning.pdf# class presentation slides 
    ├── README.md                           # Readme
    └── deepenv.yml                         # Environment (keras 2, tensorflow 1.1, etc ...)
```
### Acknowledgement
The course is based on the courses of Jeremy Howard (fast.ai) and Andrew Ng (Coursera)
* "[Deep Learning for coders](http://course.fast.ai/)" given by Jeremy Howard
* "[Deep Learning](https://fr.coursera.org/specializations/deep-learning)" given by Andrew Ng 

and the following books:
* "[Deep Learning](http://www.deeplearningbook.org/)" by Y. Bengio, I. Goodfellow and A. Courville
* "[The elements of statistical learning](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)", by H. Friedman, R. Tibshirani and T. Hastie
* "[Deep Learning with python](https://www.manning.com/books/deep-learning-with-python)" by  F. Chollet
