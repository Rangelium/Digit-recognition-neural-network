from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
import numpy as np
import cv2
import sys
import os

def load_nums_1_2():

	def create_model():
		model = Sequential()
		model.add(Conv2D(8, (3, 3), input_shape=(45, 45, 3), activation='relu'))
		model.add(MaxPooling2D((2, 2)))
		model.add(Conv2D(16, (3, 3), input_shape=(45, 45, 3), activation='relu'))
		model.add(MaxPooling2D((2, 2)))
		model.add(Conv2D(32, (3, 3), input_shape=(45, 45, 3), activation='relu'))
		model.add(MaxPooling2D((2, 2)))
		model.add(Flatten())
		model.add(Dense(625, activation='relu'))
		model.add(Dense(312, activation='relu'))
		model.add(Dense(12, activation='softmax'))
		model.summary()

		return model

	model = create_model()
	model.load_weights('trained_networks/neural_net_weights_1_2.h5')

	len_image = len(os.listdir("images")) - 3
	nums = []
	for i in range(len_image):
		img = cv2.imread('images/num_' + str(i) + '.jpg')
		img = cv2.resize(img, (45,45))
		img = img.astype('float32')
		img /= 255

		pred = model.predict(img.reshape(1, 45, 45, 3))
		ans = pred.argmax()

		nums.append(ans)

	return nums
