import cv2
import numpy as np

def get_color(frame, threshold=500):
    # Convert the BGR image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])

    # Threshold the image to get only specified colors
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Get the area of each color
    red_area = cv2.countNonZero(mask_red)
    green_area = cv2.countNonZero(mask_green)
    blue_area = cv2.countNonZero(mask_blue)

    # Determine the dominant color
    dominant_color = "Unknown"
    max_area = max(red_area, green_area, blue_area)

    textColor = (0,0,0)

   
    if max_area > threshold:
        if max_area == red_area:
            dominant_color = "Red"
            textColor = (0,0,255)
        elif max_area == green_area:
            dominant_color = "Green"
            textColor = (0,255,0)
        elif max_area == blue_area:
            dominant_color = "Blue"
            textColor = (255,0,0)

    # Draw the dominant color on the frame
    cv2.putText(frame, f"Color: {dominant_color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, textColor, 2)
    

    return dominant_color