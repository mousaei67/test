#pip install opencv-python
import cv2
import numpy as np
#from matplotlib import pyplot as plt
img = cv2.imread('img/r.jpg',0)
m,n=img.shape
img = cv2.resize(img, dsize=(700, 700))
cv2.imshow("mohsen",img)
key=cv2.waitKey(0)
if key==27:
    cv2.destroyWindow
elif key==ord("s"):
    cv2.imwrite("aaa.png",img)
    cv2.destroyAllWindows
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image')
print(img.shape)
