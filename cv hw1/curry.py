import cv2 as cv
import numpy as np

kernel = np.array([
  [0, -1, 0],
  [-1, 5, -1],
  [0, -1, 0]
])


image = cv.imread('curry.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#print(image.shape)
cv.imshow('image',image)
default = cv.filter2D(image,-1,kernel)
cv.imshow('default',default)

resulting_image = np.empty((640,960),np.uint8)
for row in range(640):
  resulting_image[row][0] = image[row][0]
for row in range(640):
  resulting_image[row][959] = image[row][959]
for col in range(960):
  resulting_image[0][col] = image[0][col]
for row in range(960):
  resulting_image[639][col] = image[639][col]

for row in range(1,638):
  for col in range(1,958):
    resulting_image[row][col] = image[row-1][col-1] * kernel[0][0] + image[row][col-1] * kernel[0][1] + image[row+1][col-1] * kernel[0][2] + image[row-1][col] * kernel[1][0] + image[row][col] * kernel[1][1] + image[row+1][col] * kernel[1][2] + image[row-1][col+1] * kernel[2][0] + image[row][col+1] * kernel[2][1] + image[row+1][col+1] * kernel[2][2]

Max = np.max(resulting_image)
Min = np.min(resulting_image)


for row in range(1,638):
  for col in range(1,958):    
			resulting_image[row][col] = (resulting_image[row][col] - Min) * 255 / (Max - Min)


cv.imshow('result',resulting_image)

cv.waitKey(0)

