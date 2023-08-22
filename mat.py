import matplotlib.pyplot as plt
import numpy as np

print("1.Line Graph\n2.Dotted line graph\n3.Dashed line graph\n"
      "4.Bar Graph\n5.(H)Bar Graph\n6.Pie Chart\n7.Scatter Graph")
a=int(input("Enter your choice ?:"))
if (a==1):
 b=int(input("Enter no of elements in x:"))
 c=[]
 for x in range(0,b):  
     element=int(input("Enter element:"))
     c.append(element)
     print("x=",c)
 plt.plot(c)
 plt.show()
elif (a==2):
 b=int(input("Enter no of elements in x:"))
 c=[]
 for x in range(0,b):  
     element=int(input("Enter element:"))
     c.append(element)
     print("x=",c)
 plt.plot(c,linestyle="dotted")
 plt.show()
elif (a==3):
 b=int(input("Enter no of elements in x:"))
 c=[]
 for x in range(0,b):  
     element=int(input("Enter element:"))
     c.append(element)
     print("x=",c)
 plt.plot(c,linestyle="dashed")
 plt.show()
elif (a==4):
 b=int(input("Enter no of elements in X & Y:"))
 c=[]
 for x in range(0,b):  
     element=int(input("Enter element of X:"))
     c.append(element)
     print("X=",c)
 f=[]
 for x in range(0,b):  
     element=int(input("Enter element of Y:"))
     f.append(element)
     print("X=",c)
     print("Y=",f)    
 plt.bar(c,f)
 plt.show()
elif (a==5):
 b=int(input("Enter no of elements in X & Y:"))
 c=[]
 for x in range(0,b):  
     element=int(input("Enter element of X:"))
     c.append(element)
     print("X=",c)
 f=[]
 for x in range(0,b):  
     element=int(input("Enter element of Y:"))
     f.append(element)
     print("X=",c)
     print("Y=",f) 
 z=input("Color?:")
 plt.barh(c,f,color=z)
 plt.show()
elif (a==6):
 b=int(input("Enter no of elements in x:"))
 c=[]
 e=[]
 for x in range(0,b):  
     element=int(input("Enter element:"))
     c.append(element)
     print("x=",c)
 for x in range(0,b):
     label=input("Enter label of Element"+str(x+1)+":")   
     e.append(label)
     print("X=",c)
     print(e)
 plt.pie(c,labels = e)
 plt.show() 
elif (a==7):
 b=int(input("Enter no of elements in X & Y:"))
 c=[]
 for x in range(0,b):  
     element=int(input("Enter element of X:"))
     c.append(element)
     print("X=",c)
 f=[]
 for x in range(0,b):  
     element=int(input("Enter element of Y:"))
     f.append(element)
     print("X=",c)
     print("Y=",f) 
 z=input("Color?:")
 plt.scatter(c,f,color=z)
 plt.show()