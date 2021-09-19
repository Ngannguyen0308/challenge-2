import cv2
import numpy as np
import utlis


path ="2.jpg"

height = 1024
width = 800
questions = 5
choices = 5
y = 150
y_H=280
x=130
x_W=350

img = cv2.imread(path)
img = cv2.resize(img,(width,height))
imgGray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray, (5,5), 1)
imgCanny= cv2.Canny(imgBlur, 10, 70)

masked = img[y:y_H, x:x_W] 
gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY_INV)[1]
boxes = utlis.splitBoxes(thresh)
#cv2.imshow("split boxes", boxes[1])
#chạy y với y_H -> mỗi lần chạy là có 5c được chấm


             

myPixelVal = np.zeros((questions,choices))
countR=0
countC=0

for masked in boxes:
    totalPixels = cv2.countNonZero(masked)
    myPixelVal[countR][countC]= totalPixels
    countC += 1
    if (countC==choices):countC=0;countR +=1
#print(myPixelVal)

myIndex =[] 
for x in range (0,questions):
    arr = myPixelVal[x]
    myIndexVal = np.where(arr==np.amax(arr))
    myIndex.append(myIndexVal[0][0])
#print(myIndex)

for elements in myIndex:
    if elements ==0:
        print('\tA',end='')
    if elements == 1:
        print('\tB',end='')
    if elements == 2:
        print('\tC',end='')
    if elements == 3:
        print('\tD',end='')
    if elements == 4:
        print('\tE',end='')







#cv2.imshow("masked", masked)
#cv2.waitKey(0)

