import cv2 as cv
import numpy as np
pic1 = cv.imread("Fig0424_a.bmp")
pic2 = cv.imread("Fig0427_a.bmp")
pic1 = cv.resize(pic1,(256,256))
pic2 = cv.resize(pic2,(256,256))
pic1 = cv.cvtColor(pic1,cv.COLOR_BGR2GRAY)
pic2 = cv.cvtColor(pic2,cv.COLOR_BGR2GRAY)
cv.imshow("a", pic1)
cv.imshow("b",pic2)
# cv.waitKey(0)
f1 = np.fft.fft2(pic1)
shifted1 = np.fft.fftshift(f1)
mag1 = np.abs(shifted1)
f2 = np.fft.fft2(pic2)
shifted2 = np.fft.fftshift(f2)
mag2 = np.abs(shifted2)
shifted1[:,:] = shifted1[:,:] / mag1 * mag2
shifted2[:,:] = shifted2[:,:] / mag2 * mag1
img1 = np.fft.ifft2(shifted1).real.astype('uint8')  
img2 = np.fft.ifft2(shifted2).real.astype('uint8')  
cv.imshow("a2", img1)
cv.imshow("b2",img2)
cv.imwrite('2.1.jpg', img1)
cv.imwrite('2.2.jpg', img2)
cv.waitKey(0)
