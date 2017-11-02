# course ENSAE-ENSAI CEPE - "Formation continue" - Deep Learning
### What is this repository for? 
Notebooks and support necessary for the "Deep Learning course given to the ENSAE-ENSAI by Hagop Boghazdeklian

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
└── course_ensae_cepe
    ├── notebooks                    # data folder contaning notebooks and utils
         ├── MNIST_CNN.ipynb         # notebook for MNIST
         └── IMDB_CRITICS.ipynb      # notebook for IMDB critics sentiment analysis
         └── CATS_VS_DOGS.ipynb      # notebook for Cats vs. Dog using Transfer Learning         
         └── utils.py                # utils necessary for the two notebooks
    ├── ENSAE                       # Course presentation slides in pdf
    ├── images                       # all support images
    ├── deepenv.yml                  # Environment (keras 2, tensorflow 1.1, etc ...)
    ├── README.md                    # Readme
```
### Acknowledgement
The course is based on the courses of Jeremy Howard (fast.ai) and Andrew Ng (Coursera)
* "Deep Learning for coders" given by Jeremy Howard [http://course.fast.ai/](http://course.fast.ai/)
* "Deep Learning" given by Andrew Ng [https://fr.coursera.org/specializations/deep-learning](https://fr.coursera.org/specializations/deep-learning)

