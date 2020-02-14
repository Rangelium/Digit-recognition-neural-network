import sys
import os

if __name__ == '__main__':
	from predict_for_networks.predict_1_1 import load_nums_1_1
	from predict_for_networks.predict_1_2 import load_nums_1_2
	from predict_for_networks.predict_2_1 import load_nums_2_1
	from predict_for_networks.predict_2_2 import load_nums_2_2
	from predict_for_networks.predict_2_3 import load_nums_2_3

	def mode(l):
		most_rep = 0
		for i in range(len(l)):
			rep = 0
			for j in range(len(l)):
				if l[i] == l[j]:
					rep += 1
			if rep > most_rep:
				most_rep = rep
				digit = l[i]
		return digit
	
	try:
		os.system(f'python3 side_img_prepare.py {sys.argv[1]}')
	except:
		os.system('rm used_images/img.png')
		os.system('gnome-paint images/img.jpg')
		os.system('clear')
	
	os.system('python3 images/image_divide.py images/img.jpg')
	os.system('cp images/img.jpg used_images/img.png')
	os.system('cp images/img_blank.jpg images/img.jpg')

	arr_of_num_array = []
	arr_of_num_array.append(load_nums_1_1())
	arr_of_num_array.append(load_nums_1_2())
	arr_of_num_array.append(load_nums_2_1())
	arr_of_num_array.append(load_nums_2_2())
	arr_of_num_array.append(load_nums_2_3())

	os.system("clear")

	num_array = []
	for i in range(len(arr_of_num_array[0])):
		tmp_list = []
		for j in range(5):
			tmp_list.append(arr_of_num_array[j][i])
		# print(tmp_list)
		num_array.append(mode(tmp_list))

	# print()
	os.system('rm images/num*')

	ans = ''
	st = ''
	for num in num_array:
		num = int(num)
		if num < 10:
			st += str(num)
		else:
			ans += st
			if num == 10:
				ans += '-'
			if num == 11:
				ans += '+'
			st = ''
	ans += st

	print(ans)
	print(f"Answer = {eval(ans)}")

else:
	print("You have't trainned neural network!")
