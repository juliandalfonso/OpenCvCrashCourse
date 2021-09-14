
import cv2
import numpy as np

img = cv2.imread('./Resources/lena.png')
kernel = np.ones((5,5),np.uint8)

#convierte a escala de grises
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#convierte a desenfocado
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)

#muestra las bordes de la imagen
imgCanny = cv2.Canny(img, 100,100)
imgDilatation = cv2.dilate(imgCanny,kernel,iterations=1)

imgEroded = cv2.erode(imgDilatation, kernel, iterations=1)

cv2.imshow('Gray image', imgGray)
cv2.imshow('image Blur', imgBlur)
cv2.imshow('image Canny', imgCanny)
cv2.imshow('image Dilation', imgDilatation)
cv2.imshow('image Erode', imgEroded)
cv2.waitKey(0)
