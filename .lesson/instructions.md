Look at main.py and find the section of the code that says "Finish these functions:" and finish them. If you run them on the provided images, your resulting image should match one of the images in the Sample results folder. Scroll past all of the unfinished functions to find some test code you can use. After you submit here, use the vertical ... in the files tabe to download a zip of the project and upload it to the assignment in Canvas and submit it there also.

Below are the functions that need finishing in case you lose one of them.

#Returns a new image that has all of a color (RED, GREEN, or BLUE given using the constants at the top of the file) removed by setting the value to 0.
def remove(image, color):
	return image
	
#Returns a new image that has only one color (RED, GREEN, or BLUE given using the constants at the top of the file) while the other two are removed by setting their values to 0.
def keepOnlyOne(image, color):
	return image

#Returns a new image that is the greyscale version of image.
def greyScale(image):
	return image

#Returns a new image that is the negative version of image (all values are subtracted from 255 so that light becomes dark, red becomes cyan, etc.).
def negate(image):
	return image
	
#Returns a new image that reflects the top half of image onto the bottom half.
def reflectTopToBot(image):
	return image

#Returns a new image that reflects the right half of the image onto the left half.
def reflectRightToLeft(image):
	return image

#Returns a new image that flips image along the left or right side. Everything should look backwards (text can help check this).
def flipHorizontal(image):
	return image

#Returns a new image that flips image along the top or bottom. Everything should look upside down.
def flipVertical(image):
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