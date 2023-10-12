# import librairies
import cv2
import pyautogui
import numpy as np
import time

# set color range
yellow_lower = np.array([17, 72, 183])
yellow_upper = np.array([179, 255, 255])

# set initial y position
previous_y = 0
previous_x = 0

#initialyse camera
cap = cv2.VideoCapture(0)
while True:
    success, frame = cap.read()
    # convert frame into hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Create mask for descriminate specific color
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    #find contour
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        area = cv2.contourArea(c)

        if area > 200:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w, y+h), (75, 100, 138), 4)

            if y < previous_y:
                print(f'Vers le haut : {y, previous_y}, area is {area}')
                pyautogui.scroll(50)
                #pyautogui.press('pageup')
                #time.sleep(0.05)

            elif y > previous_y:                
                print(f'Vers le bas : {y, previous_y}, area is {area}')
                pyautogui.scroll(-50)
                #pyautogui.press('pagedown')
                #time.sleep(0.05)

            elif x < previous_x:
                print(f'Precedant : {x, previous_x}')
                pyautogui.hotkey('alt', 'left')
            #    time.sleep(0.05)

            elif x > previous_x:
                print(f'Suivant : {x, previous_x}')
                pyautogui.hotkey('alt', 'right')
            #    time.sleep(0.05)
            
            else:
                continue

    cv2.imshow('Object', frame)
    cv2.waitKey(1)
