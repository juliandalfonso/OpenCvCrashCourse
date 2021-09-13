
import cv2

img = cv2.imread('./Resources/lena.png')

#convierte a escala de grises
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#convierte a desenfocado
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)

#muestra las bordes de la imagen
imgCanny = cv2.Canny(img, 100,100)


cv2.imshow('Gray image', imgGray)
cv2.imshow('image Blur', imgBlur)
cv2.imshow('image Canny', imgCanny)
cv2.waitKey(0)
