from random import randint
import numpy as np
import cv2
import os

for r in range(1,3):
	#############################Test bar init##############################

	labels_len = 12
	files = labels_len
	test_bar_str = "[...................................]"
	len_line = len(test_bar_str) - 2
	inc_file = int(files/len_line)
	file_num = 0
	change_sign = 1

	#############################Labels init##############################

	len_imgs = []
	for i in range(labels_len):
		len_imgs.append(len(os.listdir(f"DATA/DATASET_{str(r)}/train_data_{str(r)}/" + str(i))))

	label_train = []
	for i in range(labels_len):
		label_train += [i] * len_imgs[i]

	#############################Test bar main part##############################

		test_bar = []
		for sign in test_bar_str:
			test_bar.append(sign)

		if change_sign > len_line:
			change_sign -= 1
		
		if file_num >= inc_file:
			file_num = 0
			test_bar[change_sign] = '>'
			if change_sign != 1:
				test_bar[change_sign - 1] = '='
			change_sign += 1

		if i == files - 1:
			test_bar[-2] = '>'
			for sign in range(1, len_line):
				test_bar[sign] = '='

		test_bar_str = ''
		for sign in test_bar:
			test_bar_str += sign

		file_num += 1

		print(f"Label #{i+1}/{labels_len} \t {test_bar_str}", end='\r')

	print()
	#############################Label part main part##############################

	print()

	#############################Images part init##############################

	img_train = []

	for a in range(labels_len):

	#############################Test bar init(inside Im.part init)##############################

		files = len_imgs[a]
		test_bar_str = "[...................................]"
		len_line = len(test_bar_str) - 2
		inc_file = int(files/len_line)
		file_num = 0
		change_sign = 1

	#############################Continue of  Images init##############################

		for b in range(len_imgs[a]):
			img = cv2.imread(f'DATA/DATASET_{str(r)}/train_data_{str(r)}/' + str(a) + '/' + str(b) + '.jpg')
			img = img.astype('float32')
			img /= 255

			img_train.append(img)

	#############################Test bar main part#############################

			test_bar = []
			for sign in test_bar_str:
				test_bar.append(sign)

			if change_sign > len_line:
				change_sign -= 1
			
			if file_num >= inc_file:
				file_num = 0
				test_bar[change_sign] = '>'
				if change_sign != 1:
					test_bar[change_sign - 1] = '='
				change_sign += 1

			if b == files - 1:
				test_bar[-2] = '>'
				for sign in range(1, len_line):
					test_bar[sign] = '='

			test_bar_str = ''
			for sign in test_bar:
				test_bar_str += sign

			file_num += 1

			print(f"Image {a}: #{b+1}/{len_imgs[a]} \t {test_bar_str}", end='\r')
		print()

	#######################Randomizing#######################

	print("Starting randomizing images")
	l = len(img_train)
	arr_labels = [0 for i in range(l)]
	arr_images = [0 for i in range(l)]

	for i in range(l):
		rand = randint(0, l-1)
		while type(arr_images[rand]) != int:
			rand = randint(0, l-1)
		print(f"Image #{i}", end='\r')
		arr_images[rand], arr_labels[rand] = img_train[i], label_train[i]

	print()
	img_train = arr_images
	label_train = arr_labels
	print("Finished randomizing")

	#########################FINISHED AND SAVING########################

	label_train = np.array(label_train)
	len_total = len(label_train)
	np.save(f"DATA/DATASET_{str(r)}/labels_train_{str(r)}", label_train)
	print(f"Label file for train images with {len_total} labels prepared and saved!")

	img_train = np.array(img_train)
	np.save(f"DATA/DATASET_{str(r)}/images_train_{str(r)}", img_train)
	print()
	print(f"Train images file with {len_total} images prepared and saved!")


#########################################################################################
                                #TEST IMAGES PART#
#########################################################################################
	print()
	
	#############################Test bar init##############################

	labels_len = 12
	files = labels_len
	test_bar_str = "[...................................]"
	len_line = len(test_bar_str) - 2
	inc_file = int(files/len_line)
	file_num = 0
	change_sign = 1

	#############################Labels init##############################

	len_imgs = []
	for i in range(labels_len):
		len_imgs.append(len(os.listdir(f"DATA/DATASET_{str(r)}/test_data_{str(r)}/" + str(i))))

	label_train = []
	for i in range(labels_len):
		label_train += [i] * len_imgs[i]

	#############################Test bar main part##############################

		test_bar = []
		for sign in test_bar_str:
			test_bar.append(sign)

		if change_sign > len_line:
			change_sign -= 1
		
		if file_num >= inc_file:
			file_num = 0
			test_bar[change_sign] = '>'
			if change_sign != 1:
				test_bar[change_sign - 1] = '='
			change_sign += 1

		if i == files - 1:
			test_bar[-2] = '>'
			for sign in range(1, len_line):
				test_bar[sign] = '='

		test_bar_str = ''
		for sign in test_bar:
			test_bar_str += sign

		file_num += 1

		print(f"Label #{i+1}/{labels_len} \t {test_bar_str}", end='\r')

	print()
	#############################Label part main part##############################

	print()

	#############################Images part init##############################

	img_train = []

	for a in range(labels_len):

	#############################Test bar init(inside Im.part init)##############################

		files = len_imgs[a]
		test_bar_str = "[...................................]"
		len_line = len(test_bar_str) - 2
		inc_file = int(files/len_line)
		file_num = 0
		change_sign = 1

	#############################Continue of  Images init##############################

		for b in range(len_imgs[a]):
			img = cv2.imread(f'DATA/DATASET_{str(r)}/test_data_{str(r)}/' + str(a) + '/' + str(b) + '.jpg')
			img = img.astype('float32')
			img /= 255

			img_train.append(img)

	#############################Test bar main part#############################

			test_bar = []
			for sign in test_bar_str:
				test_bar.append(sign)

			if change_sign > len_line:
				change_sign -= 1
			
			if file_num >= inc_file:
				file_num = 0
				test_bar[change_sign] = '>'
				if change_sign != 1:
					test_bar[change_sign - 1] = '='
				change_sign += 1

			if b == files - 1:
				test_bar[-2] = '>'
				for sign in range(1, len_line):
					test_bar[sign] = '='

			test_bar_str = ''
			for sign in test_bar:
				test_bar_str += sign

			file_num += 1

			print(f"Image {a}: #{b+1}/{len_imgs[a]} \t {test_bar_str}", end='\r')
		print()

	#############################Images main part##############################

	#######################Randomizing#######################
	
	print("Starting randomizing images")
	l = len(img_train)
	arr_labels = [0 for i in range(l)]
	arr_images = [0 for i in range(l)]

	for i in range(l):
		rand = randint(0, l-1)
		while type(arr_images[rand]) != int:
			rand = randint(0, l-1)
		print(f"Image #{i}", end='\r')
		arr_images[rand], arr_labels[rand] = img_train[i], label_train[i]

	print()
	img_train = arr_images
	label_train = arr_labels
	print("Finished randomizing")

	#########################FINISHED AND SAVING########################

	label_train = np.array(label_train)
	len_total = len(label_train)
	np.save(f"DATA/DATASET_{str(r)}/labels_test_{str(r)}", label_train)
	print(f"Label file for test images with {len_total} labels prepared and saved!")

	img_train = np.array(img_train)
	np.save(f"DATA/DATASET_{str(r)}/images_test_{str(r)}", img_train)
	print()
	print(f"Train images file with {len_total} images prepared and saved!")