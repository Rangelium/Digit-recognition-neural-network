import os
import time

os.system("clear")
print("Welcome!")

while True:
	print("Type 'draw' to draw image")
	print("Type 'predict *path*' to predict from existed image")
	print("Type 'exit' to exit from programm")

	user = input()
	user_split = user.split()
	
	if user == 'draw':
		os.system("python3 predict_final.py")
		time.sleep(5)
	elif user_split[0] == 'predict':
		try:
			os.system(f"python3 predict_final.py {user_split[1]}")
			time.sleep(5)
		except:
			print("You haven't wrote path of file")
	elif user == 'exit':
		os.system('clear')
		print("Good bye!")
		break
	else:
		print("No such command!")

	time.sleep(1)
	os.system('clear')
