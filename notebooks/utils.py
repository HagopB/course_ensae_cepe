from __future__ import division,print_function
import math, os, json, sys, re
import _pickle as pickle
from glob import glob
import numpy as np
from matplotlib import pyplot as plt
from operator import itemgetter, attrgetter, methodcaller
from collections import OrderedDict
import itertools
from itertools import chain
from imp import reload

import pandas as pd
import PIL
from PIL import Image
from numpy.random import random, permutation, randn, normal, uniform, choice
from numpy import newaxis
import scipy
from scipy import misc, ndimage
from scipy.ndimage.interpolation import zoom
from scipy.ndimage import imread
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.manifold import TSNE
from sklearn.preprocessing import LabelBinarizer
from IPython.lib.display import FileLink
from keras.wrappers.scikit_learn import KerasClassifier

import tensorflow as tf
import keras
from keras import backend as K
from keras.utils.data_utils import get_file
from keras.utils import np_utils
from keras.utils.np_utils import to_categorical
from keras.models import Sequential, Model
from keras.layers import Input, Embedding, Reshape, merge, LSTM, Bidirectional
from keras.layers import TimeDistributed, Activation, SimpleRNN, GRU
from keras.layers.core import Flatten, Dense, Dropout, Lambda
from keras.regularizers import l2, l1
from keras.layers.normalization import BatchNormalization
from keras.layers.pooling import *
from keras.optimizers import SGD, RMSprop, Adam
from keras.metrics import categorical_crossentropy, categorical_accuracy
from keras.layers.convolutional import *
from keras.preprocessing import image, sequence
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.resnet50 import ResNet50
from keras.applications.vgg16 import VGG16
from keras.applications.inception_v3 import InceptionV3
from keras import applications
from scipy.misc import imread, imresize, imsave
from string import Template
from bs4 import BeautifulSoup

def load_array(fname):
    return bcolz.open(fname)[:]


def extract_img_info(xml):
    img_info = dict()
    img_info["size"] = [int(n) for n in xml.size.stripped_strings][:-1]
    img_info["filename"] = xml.find_all("filename")[0].text
    bboxes = dict()
    tmp = dict()
    for obj in xml.find_all("object"):
        img_info["tag"] = obj.find_all("name")[0].text
        for n in obj.find_all("bndbox"):
            tmp["xmin"] = int(n.find_all("xmin")[0].text)
            tmp["ymin"] = int(n.find_all("ymin")[0].text)
            tmp["width"] = int(n.find_all("xmax")[0].text) - tmp['xmin']
            tmp["height"] = int(n.find_all("ymax")[0].text) - tmp['ymin']
    img_info["bboxes"] = tmp
    return img_info

# below you'll need to provide the path of the folder where all the files are listed
def get_list_annotations(path):
    listing = sorted(os.listdir(path))
    annotations = []
    for file in listing:
        xml = open(path + file,'r')
        xml = BeautifulSoup(xml, "lxml")
        img_info = extract_img_info(xml)
        annotations.append(img_info)
    return(annotations)

def dict_to_pd(file):
    d = file
    df = pd.DataFrame([],columns=['filename','img_width','img_height','bb_x','bb_y','bb_width','bb_height'])
    for i in range(0,len(d)):
        to_add = pd.DataFrame([[d[i]['filename'],
                       d[i]['size'][0], 
                       d[i]['size'][1],
                       d[i]['bboxes']['xmin'],
                       d[i]['bboxes']['ymin'],
                       d[i]['bboxes']['width'], 
                       d[i]['bboxes']['height']]], 
                      columns=['filename','img_width','img_height','bb_x','bb_y','bb_width','bb_height'])
        to_add.set_index([[i]],inplace=True)
        df = df.append(to_add)
    return(df)

def get_batches(dirname, gen=image.ImageDataGenerator(), shuffle=True, batch_size=4, class_mode='categorical',
                target_size=(224,224)):
    return gen.flow_from_directory(dirname, target_size=target_size,
            class_mode=class_mode, shuffle=shuffle, batch_size=batch_size)

def get_data(path, target_size=(224,224)):
    batches = get_batches(path, shuffle=False, batch_size=1, class_mode=None, target_size=target_size)
    return np.concatenate([batches.next() for i in range(batches.samples)])

