
import cv2
import numpy as np

img = cv2.imread('./Resources/lambo.png')

#imprime el tamaño de la imagen
#(alto, ancho, #de canales(3=BGR))
print(img.shape)
imgResize = cv2.resize(img,(300, 200))

cv2.imshow('image', img)
cv2.imshow('image resized', imgResize)

cv2.waitKey(0)