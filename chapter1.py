
import cv2
import numpy as np

img = cv2.imread('./Resources/lambo.png')

#imprime el tamaño de la imagen
#(alto, ancho, #de canales(3=BGR))
print(img.shape)

#redimensionamos al tamaño que queremos (alto, ancho)
imgResize = cv2.resize(img,(1000, 500))

#recortamos una imagen desde 0y hasta 200y y desde 200x hasta 500x
imgCropped = img[0:200,200:500]

cv2.imshow('image', img)
cv2.imshow('image resized', imgResize)
cv2.imshow('image cropped', imgCropped)



cv2.waitKey(0)