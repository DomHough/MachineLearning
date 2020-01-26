import pandas as py
import os
import cv2
import numpy as np
from tqdm import tqdm
from keras.utils.np_utils import to_categorical
import random

path = 'D:/dom/Documents/Datasets/CatsVsDogs/train/'
path2 = 'C:/Users/Dom/Documents/Datasets/CatsVsDogs/train/'
currentPath = path

y_train = []
x_train = []

for file in tqdm(os.listdir(currentPath)):
    if 'cat' in file:
        y_train.append(0)
    elif 'dog' in file:
        y_train.append(1)
    image = cv2.imread(currentPath + file)
    image = cv2.resize(image, (128, 128))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x_train.append(image)

y_train = to_categorical(y_train)
training_data = list(zip(x_train, y_train))
random.shuffle(training_data)

x_train, y_train = zip(*training_data)
np.save('Data/x_train.npy', x_train)
np.save('Data/y_train.npy', y_train)
