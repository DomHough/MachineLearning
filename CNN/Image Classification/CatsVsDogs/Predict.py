import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
import time

xtest = np.load('Data/x_test.npy')
x_test = xtest.reshape(12500,128,128,1)
xtrain = np.load('Data/x_train.npy')
x_train = xtrain.reshape(25000,128,128,1)
model = load_model('Data/model.h5')
predictions = model.predict(x_test)

for i, prediction in enumerate(predictions):
    predict = np.argmax(prediction)
    if predict == 0:
        print('cat')
    else:
        print('dog')
    plt.imshow(xtest[i], cmap='gray')
    plt.draw()
    plt.pause(3)
