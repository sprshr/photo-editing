import numpy as np
from PIL import Image
import math
RED = 0
GREEN = 1
BLUE = 2
NUM_ROWS = 0
NUM_COLS = 1
def swapColors(image, color1, color2):
	arr = np.array(image)
	for row in range(arr.shape[0]):
		for col in range(arr.shape[1]):
			temp = arr[row][col][color1]
			arr[row][col][color1] = arr[row][col][color2]
			arr[row][col][color2] = temp
	return Image.fromarray(arr)


img  = Image.open("baby murloc.jpg")
def remove(image, color):
    img = Image.open(image)
    arr = np.array(img)
    for row in range(arr.shape[0]):
        for col in range(arr.shape[1]):
            for pixel in range(arr.shape[2]):
                if pixel == color:
                    pixel = 0
    image = Image.fromarray(arr)
    return image

remove(img, BLUE).save("ffffffff.jpg")