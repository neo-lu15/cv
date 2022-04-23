from audioop import reverse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('bridge.jpg', cv.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)
move1 = np.fft.fftshift(f) 
fr = -np.sort(-np.ravel(f) )

size = f.size

index = int(fr[int(np.round(size/4))])
# nf = np.where(f>index,f,0)
nf = f
w,h =f.shape
for i in range(w):
    for j in range(h):
        if(f[i][j] < index):
            nf[i][j]=0

move2 = np.fft.ifftshift(nf)
newfp = np.abs(move2)
cv.imshow('FFT 2D', newfp / np.max(newfp) * 255)    
ibridge = np.fft.ifft2(nf).real.astype('uint8')  
cv.imshow('IFFT GRAGH', ibridge)           
cv.imwrite("1.1.jpg",ibridge)
cv.waitKey(0)
cv.destroyAllWindows()