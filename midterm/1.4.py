import cv2 as cv
from cv2 import waitKey
import numpy as np

def MSE(pic1, pic2):
    diff = pic1 - pic2
    diff = diff *diff
    M,N,L= pic1.shape
    return diff.sum()/(M*N)

img = cv.imread('bridge.jpg')
img1 = cv.imread('1.1.jpg')
img2 = cv.imread('1.2.jpg')
img3 = cv.imread('1.3.jpg')
pic = cv.resize(img,(256,256))
pic1 = cv.resize(img1,(256,256))
pic2 = cv.resize(img2,(256,256))
pic3 = cv.resize(img3,(256,256))


print(MSE(img, img1))
print(MSE(img, img2))
print(MSE(img, img3))
cv.imshow("b",img2)
cv.waitKey(0)
