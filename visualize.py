import cv2
import numpy as np
import argparse
from random import randint
import os

def random_color():
	r = randint(0, 255)
	g = randint(0, 255)
	b = randint(0, 255)
	return [r,g,b]

def draw_box(left, right, top, bot, img, color):

	for x in range(left, right):
		img[top, x, 0] = color[0]
		img[top, x, 1] = color[1]
		img[top, x, 2] = color[2]

		img[bot, x, 0] = color[0]
		img[bot, x, 1] = color[1]
		img[bot, x, 2] = color[2]


	for y in range(top, bot):
		img[y, left, 0] = color[0]
		img[y, left, 1] = color[1]
		img[y, left, 2] = color[2]

		img[y, right, 0] = color[0]
		img[y, right, 1] = color[1]
		img[y, right, 2] = color[2]

	return img

def draw_center( center, img, color):

	longer = img.shape[0] if img.shape[0] > img.shape[1] else img.shape[1]
	radius = int(longer/100)
	half_r = int(radius/2)

	x = center[0]
	y = center[1]

	for i in range(x-half_r, x+half_r+1):
		for j in range(y-half_r, y+half_r+1):

			if i<0: i=0
			if i>=img.shape[1]: i=img.shape[1]-1
			if j<0: j=0
			if j>=img.shape[0]: j=img.shape[0]-1

			img[j,i,0] = color[0]
			img[j,i,1] = color[1]
			img[j,i,2] = color[2]

	return img

parser = argparse.ArgumentParser()
parser.add_argument('info', type=str, help='input txt path')
parser.add_argument('image', type=str, help='input image path')
parser.add_argument('out', type=str, help='outputDirName')
parser.add_argument('--draw_box', type=int, help='draw label or not', default= 1)
parser.add_argument('--draw_center', type=input, help='draw center or not', default=1)

args = parser.parse_args()

## read image
img = cv2.imread(args.image)
imgName = os.path.basename(args.image)


## read file
with open(args.info) as input_txt:
	for line in input_txt:
		if len(line) == 0:
			continue

		line = line.split(', ')
		tag = line[0]
		left = int(line[1])
		right = int(line[2])
		top = int(line[3])
		bot = int(line[4])
		center = [ int(round((left+right)/2.)), int(round((top+bot)/2.))]

		print "%s, %d, %d, %d, %d" % (tag, left, right, top, bot)

		color = random_color()
		if args.draw_box:
			img = draw_box(left, right, top, bot, img, color)

		if args.draw_center:
			img = draw_center(center, img, color)

	
	imgPath = os.path.join(args.out, imgName)
	cv2.imwrite(imgPath, img)



