#Turns off debugging
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import matplotlib.pyplot as plt
from keras.models import load_model
import tensorflow as tf
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

model = load_model('model.h5')

x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

x_test = x_test.astype('float32')

x_test /= 255

predictions = model.predict(x_test, verbose=1)
right = 0
wrong = 0
for i, prediction in enumerate(predictions):
    prediction = np.argmax(prediction)
    if prediction == y_test[i]:
        color = '\033[32m'
        right += 1
    else:
        color = '\033[31m'
        wrong += 1
    print(color, 'Image', i)
    print('Prediction', prediction)
    print('Actual', y_test[i], '\n')

    plt.imshow(x_test[i].squeeze())
    plt.draw()
    plt.pause(0.001)
    plt.clf()
    plt.cla()

print(right, "Right")
print(wrong, "Wrong")
