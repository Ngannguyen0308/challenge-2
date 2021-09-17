import cv2
import pytesseract
import pandas as pd
from os import listdir
import numpy as np
import csv


img = cv2.imread("ans.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
edge_img = cv2.Canny(blur_img, 10, 70)

contours, _ = cv2.findContours(edge_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0, 255,0), 3)

im2 = img.copy()
 
file = open("students.csv", "w+")
with open('students.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["StudentID","Surname","Firstname","Code"])
file.close()


for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 1)
     
    cropped = im2[y:y + h, x:x + w] 
    file = open("students.csv",'a')    
    text = pytesseract.image_to_string(cropped)
     
    file.write(text)
    file.write("\n")
    file.close

    cv2.imshow(cropped)
    cv2.waitKey(0)
