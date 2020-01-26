from tqdm import tqdm
import numpy as np
import os
import cv2
import random

path = 'D:/dom/Documents/Datasets/CatsVsDogs/test/'
path2 = 'C:/Users/Dom/Documents/Datasets/CatsVsDogs/test/'
currentPath = path

x_test = []

for file in tqdm(os.listdir(currentPath)):
    image = cv2.imread(currentPath + file)
    image = cv2.resize(image, (128, 128))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x_test.append(image)
random.shuffle(x_test)
np.save('Data/x_test.npy', x_test)
