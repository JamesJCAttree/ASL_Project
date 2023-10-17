import cv2

# Variables
    # Camera information
brightness_increase = -50

cap = cv2.VideoCapture(0)  # Capture object

if not cap.isOpened():  # Check if the camera was opened
    print("Error: Issue with opening the camera.")
    exit()

while True: # Runs the camera and collects information
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame.")
        break

    brightened_frame = cv2.add(frame, brightness_increase) # Increase brightness

    cv2.imshow('ASL Camera', brightened_frame) # Display the brightened frame

    if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty('ASL Camera', cv2.WND_PROP_VISIBLE) < 1: # Press 'Q' or the x button to close
        break

cap.release()
cv2.destroyAllWindows()
