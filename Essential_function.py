import cv2 as cv
img = cv.imread('media/photo/cats 2.jpg') #BGR image with three channel blue ,green and red
cv.imshow('cat',img)

# 1- Converting to grayscale(only see the intensity distribution of pixels rather than the color itself)
# gray = cv.cvtColor(image,color code )
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


# 2- Blur 
# remove some of anoise that exist in an image because of bad lighting or other
#applying a slight Blur
#use the Gaussian Blur
# (7,7) kernal size which is actually atwo by two tuple
# which basically the window size that opencv use to compute the blown the image
# this kernal size must be in odd number
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# 3- Edge Cascade
# trying to find the edges that are present in the image
# using canny edge detector
# its pretty famous in the computer vision world it is amulti step process that in volves alot of burring ,gradding computations and stuf like that   
# (125,175) threshold values
# if we pass the blur image the edge will reduced
canny = cv.Canny(img,125,175)
cv.imshow('edge cascade',canny)


# dilate an image using a specific structuring element  -iteration:repeat
#(3,3) kernal size
#dilation can be applied using several iterations of the time
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)
# eroding this dilated image to get back this structuring element
eroded = cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)


# resize 
# the cbo resize function 
#destination size ignoring the aspect ratio ( a proportional relationship between an image's width and height)
#by defalaut there is an interpolation that occurs in the background  
# this  interpolathion  method [cv.INTER_AREA] usful if you are shrinking the image to dimensions smaller than that of the original dimensions
# if you want to enlarge the image and scale the image to much larger dimensions use [cv.INTER_LINEAR] or [cv.INTER_CUBIC]  CUbic is the slowest among of all but image is much higer quality than AREA or LINER
resized = cv.resize(img,(500,500), interpolation = cv.INTER_AREA)
cv.imshow('resized',resized)

#cropping 
# that is basically by utilizing the fact that images are arrays we can employ somthing called array slicing we can sellct aportion of the image on the basis of your pixel values
#[50:200,200:400] region to croppe
cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)

