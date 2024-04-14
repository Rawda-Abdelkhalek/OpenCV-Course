import cv2 as cv

capture = cv.VideoCapture('media/vedio/dog.mp4')# method to capture the vedio takes an integer arguments like 0123 (if using webcam or camera connected to computer in most case webcam will be refereced by using the integer zero if have multiple camera you could referenced them by using the appropriate arguments 0123 )or a path to avideo file 


#using a while loop reading the vedio frame by frame
# capture.read() read the vedio frame by frame and return the frame as "frame" and boolean "isTrue" says whether the frame was successfully read or no
while True:
    isTrue, frame = capture.read()
    #method to display an individual frame 
    cv.imshow('video',frame)
    #to stop the vedio from playing indefinitely if the letter D is pressed then break out of this loop and stop displaying the video
    if cv.waitKey(20) & 0xFF==ord('d'):
        break


#release the capture pointer 
capture.release()
cv.destoryAllWindows()
