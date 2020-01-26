import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D

x_train = np.load('Data/x_train.npy')
y_train = np.load('Data/y_train.npy')

x_train = x_train.reshape(25000,128,128,1)

#Building Model
model = Sequential()

model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(128,128,1)))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))
model.add(Conv2D(64, kernel_size=(3,3),  activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))
model.add(Conv2D(128, kernel_size=(3,3),  activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))
model.add(Flatten())
model.add(Dense(2, activation='softmax'))
print(model.summary())

#Compiling Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=100, epochs=100)
model.save('Data/model.h5')
