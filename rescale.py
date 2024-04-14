#resize and rescale imges and video frames in opencv tp prevent computational strain large media files tend to store a  lot of information in it and displaying it takes up alot of processing needs that your computer needs to assign 
#so by resizing and rescalling we are actually trying to get rid of that information 
# rescaling video implies modifying its height and width to a particular height and width
# the reason for this is because while most cameras your webcam included not support going higher than its maximum capability 
# for example if cameras shoots  in 720p chances are it is not going to be able to shoot in 1080 p or higher 


import cv2 as cv

# to rescale video or image frame by particular scale value 
def rescaleframe(frame,scale=.75): #it take frames to be resized and scale value default .75
    # this method work for [imges , videos , live video] basically for everything you can use this rescale frame method
    width = int (frame.shape[1] * scale) #frame no shape of 1 is basically the width of you image 
    height = int(frame.shape[0] * scale) #frame no shape of 0 is basically the height of you image 
    #width and height are integers so we convert this floating point values to an integers
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA )

def changeRes(width,height):
    # use for live video this not going work on video that already exist
    capture.set(3,width)
    capture.set(4,height)

capture = cv.VideoCapture('media/vedio/dog.mp4')
img = cv.imread('media/photo/cat.jpg') 

imge_resized = rescaleframe(img) 

cv.imshow('cat',img)
cv.imshow('cat_resized',imge_resized)

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleframe(frame,scale=.2) 
    
    cv.imshow('video',frame)
    cv.imshow('video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destoryAllWindows()
     
    
cv.waitKey(0) 