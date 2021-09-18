import cv2
import numpy as np
import utlis


path = "1.jpg"

height = 700
width  = 700
questions = 5
choices = 5

img = cv2.imread(path)


img = cv2.resize(img,(width,height))
imgContours = img.copy()
imgBiggestContour = img.copy() 
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) 
imgCanny = cv2.Canny(imgBlur,10,70) 
#
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10) 
#
rectCon =utlis.rectContour(contours)
biggestContour = utlis.getCornerPoints(rectCon[0])
#print(biggestContour.shape)
gradePoints = utlis.getCornerPoints(rectCon[0])
#print(biggestContour)

if biggestContour.size != 0 and gradePoints.size != 0:
    cv2.drawContours(imgBiggestContour, biggestContour, -1, (0, 255, 0), 20) 
    cv2.drawContours(imgBiggestContour, gradePoints, -1, (255, 0, 0), 20) 

    biggestContour= utlis.reorder(biggestContour)
    gradePoints = utlis.reorder(gradePoints)

    pts1 = np.float32(biggestContour) 
    pts2 = np.float32([[0, 0],[width, 0], [0, height],[width, height]]) 
    matrix = cv2.getPerspectiveTransform(pts1, pts2) 
    imgWarpColored = cv2.warpPerspective(img, matrix, (width, height)) 


    ptG1 = np.float32(gradePoints) 
    ptG2 = np.float32([[0, 0],[325, 0], [0, 150],[325, 150]]) 
    matrixG = cv2.getPerspectiveTransform(ptG1, ptG2) 
    imgGradeDisplay = cv2.warpPerspective(img, matrix, (width, height)) 
    #cv2.imshow("Grade", imgGradeDisplay)


    imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWarpGray, 170, 255,cv2.THRESH_BINARY_INV )[1] 
    boxes = utlis.splitBoxes(imgThresh)
    #cv2.imshow("Test", boxes[3])
         
    countR=0
    countC=0
    myPixelVal = np.zeros((questions,choices))

    for image in boxes:
        #cv2.imshow(str(countR)+str(countC),image)
        totalPixels = cv2.countNonZero(image)
        myPixelVal[countR][countC]= totalPixels
        countC += 1
        if (countC==choices):countC=0;countR +=1
    #print(myPixelVal)


    myIndex =[] 
    for x in range (0,questions):
        arr = myPixelVal[x]
        myIndexVal = np.where(arr==np.amax(arr))
        #print(myIndexVal[0])
        myIndex.append(myIndexVal[0][0])
    print(myIndex)
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

            
imgBlank = np.zeros_like(img)
imgArray = ([img,imgGray,imgBlur,imgCanny],[imgContours,imgBiggestContour,imgWarpColored,imgBlank ])
imgStack = utlis.stackImages(imgArray,0.5)



cv2.imshow("Stacked image", imgStack )
cv2.waitKey(0)
