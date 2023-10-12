import cv2

img_bgr = cv2.imread('lena.png')

#display
cv2.imshow('BGR', img_bgr)
cv2.imshow('RGB', cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
cv2.imshow('HSV', cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV))
cv2.imshow('LAB', cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB))
cv2.imshow('LUV', cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LUV))
cv2.waitKey(0)
