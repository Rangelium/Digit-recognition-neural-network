import os

if os.path.isfile("DATA/DATASET_2/images_train_2.npy"):
	from keras.models import Sequential
	from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout
	import numpy as np
	import cv2

	img_train = np.load("DATA/DATASET_2/images_train_2.npy")
	label_train = np.load("DATA/DATASET_2/labels_train_2.npy")

	img_test = np.load("DATA/DATASET_2/images_test_2.npy")
	label_test = np.load("DATA/DATASET_2/labels_test_2.npy")

	model = Sequential()
	model.add(Conv2D(16, (2, 2), input_shape=(45, 45, 3), activation='relu'))
	model.add(MaxPooling2D((2, 2)))
	model.add(Conv2D(32, (2, 2), input_shape=(45, 45, 3), activation='relu'))
	model.add(MaxPooling2D((2, 2)))
	model.add(Flatten())
	model.add(Dense(2025, activation='relu'))
	model.add(Dense(12, activation='softmax'))
	model.compile(optimizer='adam', 
	              loss='sparse_categorical_crossentropy', 
	              metrics=['accuracy'])
	model.fit(x=img_train,y=label_train, epochs=2)
	model.evaluate(img_test, label_test)

	model.save_weights('trained_networks/neural_net_weights_2_1.h5')

	test_loss, test_accuracy = model.evaluate(img_test, label_test)
	print('Test loss: %.4f accuracy: %.4f' % (test_loss, test_accuracy))

else:
	print("You have't prepared dataset for training!")
