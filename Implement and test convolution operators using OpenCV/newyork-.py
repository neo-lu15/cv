import cv2 as cv
import numpy as np

kernel = np.array([
  [-1, -1, -1],
  [-1, 8, -1],
  [-1, -1, -1]
])

image = cv.imread('newyork.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('image',image)
default = cv.filter2D(image,-1,kernel)
cv.imshow('default',default)

resulting_image = np.empty((1066,1600),np.uint8)
for row in range(1066):
  resulting_image[row][0] = image[row][0]
for row in range(1066):
  resulting_image[row][1599] = image[row][1599]
for col in range(1600):
  resulting_image[0][col] = image[0][col]
for row in range(1600):
  resulting_image[1065][col] = image[1065][col]

for row in range(1,1064):
  for col in range(1,1598):
    resulting_image[row][col] = image[row-1][col-1] * kernel[0][0] + image[row][col-1] * kernel[0][1] + image[row+1][col-1] * kernel[0][2] + image[row-1][col] * kernel[1][0] + image[row][col] * kernel[1][1] + image[row+1][col] * kernel[1][2] + image[row-1][col+1] * kernel[2][0] + image[row][col+1] * kernel[2][1] + image[row+1][col+1] * kernel[2][2]

#Max = np.max(resulting_image)
#Min = np.min(resulting_image)


#for row in range(1,1064):
 # for col in range(1,1598):    
#			resulting_image[row][col] = (resulting_image[row][col] - Min) * 255 / (Max - Min)
#print(image.shape)

cv.imshow('result',resulting_image)

cv.waitKey(0)
