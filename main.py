from tkinter import READABLE
import numpy as np
from PIL import Image
import math

#Color indicies (colors are tuples in the form: [ red, green, blue])
RED = 0
GREEN = 1
BLUE = 2
NUM_ROWS = 0
NUM_COLS = 1

#Returns the distance between 2 color tuples
def getColorDistance(c1, c2):
	r1, g1, b1 = c1
	r2, g2, b2 = c2
	rv = (0 + r2 - r1) ** 2
	gv = (0 + g2 - g1) ** 2
	bv = (0 + b2 - b1) ** 2
	return math.sqrt(rv + gv + bv)

#Returns a new image that sets color to have value for the entire image
def setColor(image, color, value):
	arr = np.array(image)
	for row in range(arr.shape[0]):
		for col in range(arr.shape[1]):
			arr[row][col][color] = value
	return Image.fromarray(arr)

#Returns a new image that swaps the values of color1 and color2 in image.
def swapColors(image, color1, color2):
	arr = np.array(image)
	for row in range(arr.shape[0]):
		for col in range(arr.shape[1]):
			temp = arr[row][col][color1]
			arr[row][col][color1] = arr[row][col][color2]
			arr[row][col][color2] = temp
	return Image.fromarray(arr)

#Returns a new image that is the sepia version of image.
def sepia(image):
	arr = np.array(image)
	for row in range(arr.shape[NUM_ROWS]):
		for col in range(arr.shape[NUM_COLS]):
			r,g,b = arr[row][col]
			sr = .393 * r + .769 * g + .189 * b
			sg = .349 * r + .686 * g + .168 * b
			sb = .272 * r + .534 * g + .131 * b
			sr = min (255, int(sr))
			sg = min (255, int(sg))
			sb = min (255, int(sb))
			arr[row][col] = [sr, sg, sb]
	return Image.fromarray(arr)

#Returns a new image that is half the height and half the width of the old image:
def shrink(image):
	old_arr = np.array(image)
	rows = old_arr.shape[NUM_ROWS] // 2
	cols = old_arr.shape[NUM_COLS] // 2
	arr = np.empty( [rows, cols, 3], dtype = np.uint8 )
	for row in range(rows):
		for col in range(cols):
			r1, g1, b1 = old_arr[2 * row][2 * col]
			r2, g2, b2 = old_arr[2 * row][2 * col + 1]
			r3, g3, b3 = old_arr[2 * row + 1][2 * col]
			r4, g4, b4 = old_arr[2 * row + 1][2 * col + 1]
			r = (0 + r1 + r2 + r3 + r4) // 4
			g = (0 + g1 + g2 + g3 + g4) // 4
			b = (0 + b1 + b2 + b3 + b4) // 4
			arr[row][col] = [r,g,b]
	return Image.fromarray(arr)


	
#Finish these functions:

#Returns a new image that has all of a color (RED, GREEN, or BLUE given using the constants at the top of the file) removed by setting the value to 0.
def remove(image, color):
    arr = np.array(image)
    for row in range(arr.shape[NUM_ROWS]):
        for col in range(arr.shape[NUM_COLS]):
            arr[row][col][color] = 0
    image = Image.fromarray(arr)
    return image
	
#Returns a new image that has only one color (RED, GREEN, or BLUE given using the constants at the top of the file) while the other two are removed by setting their values to 0.
def keepOnlyOne(image, color):
	arr = np.array(image)
	for row in range(arr.shape[NUM_ROWS]):
		for col in range(arr.shape[NUM_COLS]):
			if color != RED:
				arr[row][col][RED] = 0
			if color != GREEN:
				arr[row][col][GREEN] = 0
			if color != BLUE:
				arr[row][col][BLUE] = 0
	image = Image.fromarray(arr)
	return image

#Returns a new image that is the greyscale version of image.
def greyScale(image):
	arr = np.array(image)
	for row in range(arr.shape[NUM_ROWS]):
		for col in range(arr.shape[NUM_COLS]):
			r,g,b = arr[row][col]
			avg = r * 0.2126 + g * 0.7152 + b * 0.0722
			avg = int(avg)
			arr[row][col] = [avg, avg, avg]
	image = Image.fromarray(arr)
	return image

#Returns a new image that is the negative version of image (all values are subtracted from 255 so that light becomes dark, red becomes cyan, etc.).
def negate(image):
	arr = np.array(image)
	for row in range(arr.shape[NUM_ROWS]):
		for col in range(arr.shape[NUM_COLS]):
			r,g,b = arr[row][col]
			arr[row][col] = [255-r, 255-g, 255-b]
			image = Image.fromarray(arr)
	return image
	
#Returns a new image that reflects the top half of image onto the bottom half.
def reflectTopToBot(image):
    arr = np.array(image)
    midLine = arr.shape[NUM_ROWS] // 2
    n = 0
    for row in range(midLine):
        n += 1
        arr[midLine + n] = arr[midLine - n]
    image = Image.fromarray(arr)
    return image
#Returns a new image that reflects the right half of the image onto the left half.
def reflectRightToLeft(image):
    arr = np.array(image)
    midLine = arr.shape[NUM_COLS] // 2
    for row in range(arr.shape[NUM_ROWS]):
        n = 0
        for col in range(midLine-1):
            n += 1
            arr[row][midLine - n] = arr[row][midLine + n]
    image = Image.fromarray(arr)
    return image

#Returns a new image that flips image along the left or right side. Everything should look backwards (text can help check this).
def flipHorizontal(image):
    arr = np.array(image)
    for row in range(arr.shape[NUM_ROWS]):
        arr[row] = arr[row][::-1]
    image = Image.fromarray(arr)
    return image

#Returns a new image that flips image along the top or bottom. Everything should look upside down.
def flipVertical(image):
    arr = np.array(image)
    arr = arr[::-1]
    image = Image.fromarray(arr)
    return image

#Returns a new image that has sticker (a smaller picture) placed on top of image with the upper left corner at x and y.
def addSticker(image, sticker, x, y):
	return image

#Returns a new image that is a black and white file that vaguely shows the outline of objects in image by using a given color distance threshold (dist). Hint: check the pixel below and the pixel to the right of the current pixel. If either is different enough, then it is probably an edge.
def edgesOnly(image, dist):
	return image

#Returns a new image that has the solid background color (key) of front_image replaced by the corresponding pixels from back_image with the given color distance threshold (dist).
def chromaKey(front_image, back_image, key, dist):
	return image

#Returns a new image that does whatever you want to image. The more creative the better.
#Customize the header as needed
def finalFilter(image):
	return image
	
#use/modify this code to test your functions:
img = Image.open('baby murloc.jpg')
img2 = Image.open('green screen image.jpg')
img3 = Image.open('thumbs up.png')

# remove(img, RED).save('no red.jpg')
# remove(img, GREEN).save('no green.jpg')
# remove(img, BLUE).save('no blue.jpg')

# keepOnlyOne(img, RED).save('only red.jpg')
# keepOnlyOne(img, GREEN).save('only green.jpg')
# keepOnlyOne(img, BLUE).save('only blue.jpg')

# greyScale(img).save('grey.jpg')

# negate(img).save('negated.jpg')

# reflectTopToBot(img).save('top to bot.jpg')

# reflectRightToLeft(img).save('right to left.jpg')

# flipHorizontal(img).save('flip horizontal.jpg')

# flipVertical(img).save('flip vertical.jpg')

# addSticker(img, img3, 460, 350).save('added sticker.jpg')

# edgesOnly(img2, 20).save('edges only.jpg')

# chromaKey(img2, img, [53,189,13], 100).save('chroma key.jpg')

# finalFilter(img).save('final filter.jpg')