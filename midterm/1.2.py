from audioop import reverse
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def fft(arr):
    f = np.fft.fft2(arr)
    move1 = np.fft.fftshift(f) 
    fr = -np.sort(-np.ravel(f) )
    size = f.size
    index = int(fr[int(np.round(size/4))])
    nf = f
    w,h =f.shape
    for i in range(w):
        for j in range(h):
            if(f[i][j] < index):
                nf[i][j]=0
    move2 = np.fft.ifftshift(nf)
    newfp = np.abs(move2)
    # cv.imshow('FFT 2D', newfp / np.max(newfp) * 255)    
    ibridge = np.fft.ifft2(nf).real.astype('uint8')
    return ibridge 


img = cv.imread('bridge.jpg', cv.IMREAD_GRAYSCALE)
for i in range(16):
    for j in range(16):
        width = i*16
        height = j*16
        img[width:width+16,height:height+16] = fft(img[width:width+16,height:height+16])

cv.imshow('IFFT GRAGH', img)           
cv.imwrite("1.2.jpg",img)
cv.waitKey(0)
cv.destroyAllWindows()