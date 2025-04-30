import cv2 as cv 
import numpy as np 

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output1.avi', fourcc, 20.0, (640, 480))
# save krne k liye

if not cap.isOpened(): 
    print("not able to open camera!") 
    exit()

while True: 
    ret,frame = cap.read()
    # ret will have True if frame is captured otherwise False 
    # frame has single short image frame in the form of pixel
    if not ret:
        break
    cv.imshow("capturing your video ",frame)
    
    if cv.waitKey(1) & 0xFF == ord('x'):
        break
cap.release()
cv.destroyAllWindows()  