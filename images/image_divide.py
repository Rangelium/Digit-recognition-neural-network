from PIL import Image
import sys

def crop(image_obj, coords, saved_location):

    cropped_image = image_obj.crop(coords)

    cropped_image.save(saved_location)

def line(image_obj, x, y):

	pix = image_obj.load()
	coordinates = []
	min = pix[0,0][0] + pix[0,0][1] + pix[0,0][2]
	max = min + 70
	if(min > 70):
		min -= 70
	else:
		min = 0

	flag = 1
	flag2 = 0
	for i in range(0, x):
		counter = 0
		for j in range(0, y):
			test = pix[i,j][0] + pix[i,j][1] + pix[i,j][2]
			if( (test < min or test > max) and flag == 1 ):
				coordinates.append(i - 1)
				flag = 0
				flag2 = 1
			if( (test >= min and test < max)):
				counter += 1
		if( counter == height and flag2 == 1):
			coordinates.append(i)
			flag = 1
			flag2 = 0


	return coordinates

def square(image_name):

	img = Image.open(image_name)
	pix = img.load()
	x, y = img.size
	counter = (y - x) / 2
	res = Image.new('RGB',(y,y), color =  pix[0,0])
	pix2 = res.load()

	for i in range( x ): #x
		for j in range( y ): #y
			pix2[i+counter,j] = pix[i,j]

	res.save(image_name)

img = Image.open("images/img.jpg")
width = img.size[0]
height = img.size[1]

coordinates = line(img, width, height)
names = []
ext = '.jpg'
for i in range(int(len(coordinates) / 2)):
	name = 'images/num_' + str(i) + ext
	names.append(name)
	crop(img, (coordinates[2*i], 0, coordinates[2*i+1], height), name)
	res_name = 'final_'+str(i)+ext
	square(name)


