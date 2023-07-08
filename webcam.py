import cv2

cap = cv2.VideoCapture(0)


 
 
# Loop forever (or until break)
while True:
    # Read the a frame from webcam
    _, frame = cap.read()
    frame = cv2.resize(frame, (648, 480))
    frame = cv2.flip(frame, 1)
 
    # Show the frame in a window
    cv2.imshow('WebCam', frame)
 
    # Check if q has been pressed to quit
    if cv2.waitKey(1) == ord('q'):
        break