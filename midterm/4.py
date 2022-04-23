import cv2 as cv
import numpy as np

img = cv.imread('bridge.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
while True:
    img = cv.GaussianBlur(img, (3, 13), 0)
    f1 = np.fft.fft2(img)
    shifted1 = np.fft.fftshift(f1)
    mag = np.abs(shifted1)
    cv.imshow('a', np.log(mag + 1))
    key = cv.waitKey(10)
    if key == ord('q'):
        break

img = cv.imread('bridge.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
while True:
    img = cv.medianBlur(img, 13)
    cv.imshow('b', img)
    key = cv.waitKey(10)
    if key == ord('q'):
        break