import numpy as np
a=np.array([[[1,2,3,4],[4,5,6,7],[4,5,6,7]],[[1,2,3,4],[4,5,6,7],[4,5,6,7]]])
b=[1,3,5,7,8] #list
print(b)
print (a)
print(np.ndim(a))#dimension func
print(np.size(a))
print(len(a))
print(a.shape)
c=a.reshape(3,2,4)
print(c)
d = np.array_split(a,6)
print(d)