import cv2
import numpy as np

# Step 1: Capture video from webcam (device 0)
cap = cv2.VideoCapture(0)

# Step 2: Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Step 3: Video capture loop
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to grayscale
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert back to 3 channels for saving (VideoWriter expects 3-channel image)
    img_gray_3ch = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

    # Write the frame
    out.write(img_gray_3ch)

    # Show the frame
    cv2.imshow("Webcam", img_gray)

    # Exit when 'x' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Step 4: Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
