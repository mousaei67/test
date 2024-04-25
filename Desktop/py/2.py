import numpy as np
a=np.array([[1,2,3,4,55,60,70,80,90],[5,6,7,8,66,99,88,100,110]])
#i=0
#print(a.shape[0])
aa=np.zeros([2,9])
#print(aa)
for  i in range(a.shape[0]) :
 for j in range(a.shape[1]):
     if a[i][j]>=60 :
        aa[i][j]=a[i][j]

     print(aa[i][j])
 print("\n")
