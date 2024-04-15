import cv2 as cv
import numpy as np
img = cv.imread('media/photo/group 1.jpg')
cv.imshow('cat',img)
#there are two way to draw an on images 
#1-drawing on standalone images like "group 1.jpg" 
#2- create a dummy image or blank image to work with 
# to create a blank image  we will use to draw on 
#(500,500,3) shape(height ,width,number of color chanals) 
#data type : dtype='uint8' basiclly data type of an image
blank = np.zeros((500,500,3), dtype= 'uint8')
cv.imshow('blank',blank)


#1.paint the image a certain color 
# -[:] referance all pixels 
# -  0,255,0 paint inter image grean
# -color a certain portion of the image by giving it arange of pixels blank[200:300,300:400] 
# blank[:] = 0,255,0
# cv.imshow ('green',blank)

# 2-Draw a Rectangle 
# -cv.rectangle(image,pt1,pt2,color,thickness)
# -(thickness=cv.FILLED) or (-1) fills in the rectangle
# -(250,500) this is afixed shape we can replace it with 
# -(image.shape[1]//2,image.shape[0]//2)  this will draw fill square from origen in the image(dimensions of half the orginal image)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2) ,(0,255,0),thickness=cv.FILLED) 
cv.imshow('Rectangle',blank)


# 3-Draw a Circule
#  -cv.circle(image,center,radius(pixel),color,thickness)
#  -thickness=-1 means fill with color
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
cv.imshow('circle',blank)


# 4- Draw a line
# -cv.line(image,pt1,pt2,color,thickness)
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2) ,(0,255,255),thickness=3)
cv.imshow('line',blank) 

# 5-how to writ text on an image 
#cv.putText(image,'text',origin,fontFace,fontscale,color,thickness)
text_p = np.zeros((500,500,3), dtype= 'uint8')

cv.putText(text_p,' hello I am Peg_Ro ',(60,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,200,55),1)
cv.imshow('text',text_p)
cv.waitKey(0)
