import matplotlib.pyplot as plt
import numpy as np

n=int(input("Enter numbers if Data Points: "))

x=[]   # array to store x
xSq=[]   # array to store x square
y=[]     # array to store y
xy=[]    # array to store x.y


i=0
while i<n:                                # loop to collect x co-ordinat of Data points and store in array (x)
    x.append(float(input(f"\nEnter x{i+1}: ")))
    y.append(float(input(f"Enter y{i+1}: ")))
    i+=1 
Sum_X=sum(x)     # Sums all the valus stored in array (x)
Sum_Y=sum(y)     # Sums all the valus stored in array (y)

xSq=[x**2 for x in x]
Sum_Xsq=sum(xSq)
Sum_XY=sum([x[i]*y[i] for i in range(0,n)])
      
m=(n*Sum_XY - Sum_X*Sum_Y)/(n*Sum_Xsq - (Sum_X)**2)     # Calculating Slope
c=(Sum_Y - (m*Sum_X))/n     #Calculating Intercept

print(f'''\nSum_X: {Sum_X}
Sum_XY: {Sum_XY}
Slope m= {m}
Intercept c= {c}''')
print("\nFinal equation of the Best fit line is:")
if c>=0:
    print(f"y={m}x+{c}")
else:
    print(f"y={m}x3{c}")
    
plt.scatter(x,y,color='blue',marker="o",label="Data Points")
x=np.linspace(min(x),max(x),1000)
y_pred=m*x+c
plt.plot(x,y_pred,color='red', label="Best Fit Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.title("Linear Regression: Best fit Line")
plt.legend()
plt.grid(linestyle=":")
plt.show()
