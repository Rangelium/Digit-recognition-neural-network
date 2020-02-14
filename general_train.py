import os

if os.path.isfile("DATA/DATASET_1/images_train_1.npy"):
	print("Preparing first network")
	os.system("python3 networks_train/train_1_1.py")
	os.system("clear")

	print("Preparing second network")
	os.system("python3 networks_train/train_1_2.py")
	os.system("clear")

	print("Preparing third network")
	os.system("python3 networks_train/train_2_1.py")
	os.system("clear")

	print("Preparing fourth network")
	os.system("python3 networks_train/train_2_2.py")
	os.system("clear")

	print("Preparing fifth network")
	os.system("python3 networks_train/train_2_3.py")
	os.system("clear")

	print("All 5 networks prepared!")
else:
	print("You have't prepared dataset for training!")