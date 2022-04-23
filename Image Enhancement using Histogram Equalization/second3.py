from tkinter import image_names
import cv2
import numpy as np
import matplotlib.pyplot as plt

def myHistEq(img):
    width, height, depth = img.shape
    total = width * height
    begin = [[0 for col in range(width)] for row in range(height)]
    cnt = [0] * 256
    for i in range(width):
        for j in range(height):
            cnt[img[i][j]] += 1
    for i in range(1,256):
        cnt[i] += cnt[i-1]
    cnt = cnt * 255 / total
    target = begin
    for i in range(width):
        for j in range(height):
            target[i][j] = cnt[img[i][j]]
    return target


img_bgr = cv2.imread("mp2a.jpg",cv2.IMREAD_COLOR)
image = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2YCrCb)
(y, cb, cr) = cv2.split(image)
mydst = myHistEq(y)   
cvdst = cv2.equalizeHist(y) 
merged1 = cv2.merge([mydst,cb,cr])
merged2 = cv2.merge([cvdst,cb,cr])
image1 = cv2.cvtColor(merged1,cv2.COLOR_YCrCb2BGR)
image2 = cv2.cvtColor(merged2,cv2.COLOR_YCrCb2BGR)
cv2.imwrite("mp2aYcvdst.jpg",image2)
cv2.imwrite("mp2aYmydst.jpg",image1)