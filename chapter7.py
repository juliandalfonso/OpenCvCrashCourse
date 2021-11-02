import cv2



def empty(a):
    pass



path = 'Resources/lambo.png'
cv2.namedWindow('Trackbars')
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue min", "Trackbars",0,179,empty)
cv2.createTrackbar("Hue max", "Trackbars",179,179,empty)
cv2.createTrackbar("sat min", "Trackbars",0,255,empty)
cv2.createTrackbar("sat max", "Trackbars",255,255,empty)
cv2.createTrackbar("val min", "Trackbars",0,255,empty)
cv2.createTrackbar("val max", "Trackbars",255,255,empty)



img =cv2.imread(path)


imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.imshow("Original", img)
cv2.imshow("HSV", imgHSV)
cv2.waitKey(0)