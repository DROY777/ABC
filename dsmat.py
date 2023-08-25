import matplotlib.pyplot as plt
import numpy as np
#Violin plot
'''total=[20,10,26,35,49,56,23,49,89,67]
order=[50,60,86,38,43,53,27,39,87,67]
discount=[40,20,66,75,89,55,33,89,39,67]
data=list([total,order,discount])
fig=plt.figure(figsize=(7,7))
ax1=plt.subplot(121)
ax2=plt.subplot(122)
ax1.violinplot(data,showmeans=True,showmedians=False)
ax2.violinplot(data,showmeans=True,showmedians=False)
plt.show()'''

#Quiver plot
'''x=[0,0]
y=[0,0]
x_d=[1,0]
y_d=[1,-1]
fig=plt.figure(figsize=(5,5))
ax1=plt.subplot()
ax1.quiver(x,y,x_d,y_d,scale=3)
plt.show()'''

#Stack plot
'''a=range(0,5)
b=[[1,2,3,4,5],[2,3,4,5,6],[6,7,8,9,10]]
f=plt.figure(figsize=(5,5))
ax=plt.subplot()
ax.stackplot(a,b)   
plt.show()'''

#Box plot
'''t=[12,13,12,34,34,23,67,56,34]
f=plt.figure(figsize=(3,3))
ax=plt.subplot()
ax.boxplot(t)
plt.show()'''

#StreamPlot
'''x=np.arange(0,2.2,0.1)
y=np.arange(0,2.2,0.1)
X,Y=np.meshgrid(x,y)
u=np.cos(X)*y
v=np.sin(y)*Y
fig=plt.figure(figsize=(5,5))
ax1=plt.subplot()
ax1.streamplot(X,Y,u,v, density=1)
plt.show()'''

import seaborn as sns
'''titanic=sns.load_dataset("titanic")
print(titanic)
sns.countplot(y='class',hue='who',data=titanic)
plt.show()
sns.countplot(x='class',data=titanic)
plt.show()'''

#HEAT MAP
'''a=[
   [200,45,34],
   [66,23,77],
   [34,22,100] 
  ]
sns.heatmap(a, annot=True)
plt.show()'''