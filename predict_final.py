import os

if os.path.isfile("trained_networks/neural_net_weights_2_3.h5"):
	from predict_for_networks.predict_1_1 import load_nums_1_1
	from predict_for_networks.predict_1_2 import load_nums_1_2
	from predict_for_networks.predict_2_1 import load_nums_2_1
	from predict_for_networks.predict_2_2 import load_nums_2_2
	from predict_for_networks.predict_2_3 import load_nums_2_3
	from statistics import mode

	os.system('rm used_images/img.png')
	os.system('gnome-paint images/img.jpg')
	os.system('python3 images/image_divide.py images/img.jpg')
	os.system('cp images/img.jpg used_images/img.png')
	os.system('cp images/img_blank.jpg images/img.jpg')
	os.system('clear')
		
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
		print(tmp_list)
		try:
			num_array.append(mode(tmp_list))
		except:
			num_array.append(tmp_list[0])

	print()
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
