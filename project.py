import os
import time

os.system("clear")
print("Welcome!")

while True:
	print("Type 'image' to draw image")
	print("Type 'train' for train network")
	print("Type 'prepare' to prepare dataset for training")
	print("Type 'exit' to exit from programm")

	user = input()
	
	if user == 'image':
		os.system("python3 predict_final.py")
	if user == 'prepare':
		os.system("python3 database.py")
	if user == 'train':
		os.system("python3 general_train.py")
	if user == 'exit':
		os.system('clear')
		print("Good bye!")
		break

	time.sleep(6)
	os.system('clear')
