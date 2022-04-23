from audioop import reverse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread('bridge.jpg', cv.IMREAD_GRAYSCALE)

nimg = np.zeros((128,128),dtype=np.uint8)

for i in range(128):
    for j in range(128):
        nimg[i][j]  = img[i*2][j*2]/4+img[i*2+1][j*2]/4+img[i*2][j*2+1]/4+img[i*2+1][j*2+1]/4

print(nimg.shape)

f = np.fft.fft2(nimg)
move1 = np.fft.fftshift(f)
#print(move1.shape) 
nnimg = np.zeros((256,256))
nnimg[ 64:192, 64:192] =move1
move2 = np.fft.ifftshift(nnimg)
#print(move2.shape)
newfp = np.abs(move2)  
nnimg= np.fft.ifft2(newfp).real.astype('uint8')
#print(nnimg.shape)
cv.imshow('bridge.jpg',img) 
cv.imshow('IFFT GRAGH', nnimg)           
cv.imwrite("1.3.jpg",nnimg)
cv.waitKey(0)
#cv.destroyAllWindows()