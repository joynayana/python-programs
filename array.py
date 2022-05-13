import numpy as np
#one diamential array
a=np.array([1,2,3,4,5])
print(a)
# check numpy version
print(np.__version__)
#2D array
b=np.array([[1,2,3,4],[3,4,6,7]])
print(b)
#check array diamension
print("this array diamention is:",b.ndim)
#accessing array element
print(a[0])
print(b[0,1])
print(b[1,2])
#to  print last element
print(a[-1])
print(b[0,-1])
print(b[1,-1])
#arry slicing 2D
#print(b[0,1:3])
#print(b[1,1:3])
print(b[0:2,1:4])
