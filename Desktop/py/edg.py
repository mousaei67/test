import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
im = cv.imread('img/R.jpg',0)
im = cv.resize(im, dsize=(700, 700))
im2=im


cv.imshow("mohsen",im)
key=cv.waitKey(3000)
if key==27:
    cv.destroyWindow
print ("mohsen mousaei")
#plt.subplot(121),plt.imshow(im,cmap = 'gray')
#plt.title('Original Image')
#plt.show()

m,n=im.shape
kx=np.array([[-1,5,0],[4,6,3],[2,11,12]])
k=np.array([[-1,-1,0],[-1,0,1],[0,1,1]])
edge=np.zeros((m,n))
print(m,n)

for i in range(m-2):
    
    for j in range(n-2):
        
        
        l=(im[i,j]*k[0,0])+(im[i+1,j]*k[1,0])+(im[i+2,j]*k[2,0])+(im[i,j+1]*k[0,1])+(im[i+1,j+1]*k[1,1])+(im[i+2,j+1]*k[2,1])+(im[i,j+2]*k[0,2])+(im[i+1,j+2]*k[1,2])+(im[i+2,j+2]*k[2,2]) 
      
        if l>50:
            edge[i,j]=1
            

cv.imshow("aaa",edge)  
cv.waitKey(0)    
plt.subplot(111),plt.imshow(edge,cmap = 'gray')
plt.title('Original Image')

plt.show()
print("finish")