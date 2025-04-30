import time
import cv2
import numpy as np

# Step 1: Capture video from webcam (device 0)
cap = cv2.VideoCapture('output.avi')
while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam",frame)
    time.sleep(1/20)
   
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break



cv2.destroyAllWindows()