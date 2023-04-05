import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(10,200), cv2.FONT_HERSHEY_COMPLEX, 1.3,(255,255, 255))
cv2.putText(img,"Mercury",(120, 200), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))
cv2.putText(img,"Venus",(200, 180), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))
cv2.putText(img,"Earth",(300, 170), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))
cv2.putText(img,"Mars",(400, 180), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))
cv2.putText(img,"Jupiter",(550, 60), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))
cv2.putText(img,"Saturn",(750, 130), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))
cv2.putText(img,"Uranus",(950, 140), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))
cv2.putText(img,"Neptune",(1120, 150), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255,255, 255))

cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_system_with_names", img)
