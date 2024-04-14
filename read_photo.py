#  Read an imgs wih opencv
import cv2 as cv
# to read an image this method takes in a path to an image and return it as a matrix of pixels i capture this image in "img" variable  
img = cv.imread('media/photo/cat.jpg') 

# show method it displays the image as new window so it take two parameters the name of the window and the actual matrix of pixels to display
cv.imshow('cat',img)

#keyboard binding function waits for apecific delay (time in milliseconds)for a key to be pressed  0:mean wait for infinite amount of time for a keyboard key to pressed
cv.waitKey(0) 