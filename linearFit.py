import matplotlib.pyplot as plt
import numpy as np

n=int(input("Enter numbers if Data Points: "))

x=[]   # array to store x
y=[]     # array to store y

i=0
while i<n:                                # loop to collect x co-ordinat of Data points and store in array (x)
    x.append(float(input(f"\nEnter x{i+1}: ")))
    y.append(float(input(f"Enter y{i+1}: ")))
    i+=1

x=np.array(x)
y=np.array(y)

sumX=sum(x)     # Sums all the valus stored in array (x)
sumY=sum(y)     # Sums all the valus stored in array (y)

sumXsq=sum(x**2)
sumXY=sum(x*y)
      
m=(n*sumXY - sumX*sumY)/(n*sumXsq - (sumX)**2)     # Calculating Slope
c=(sumY - (m*sumX))/n     #Calculating Intercept

print(f'''\nsumX: {sumX}
sumXY: {sumXY}
Slope m= {m}
Intercept c= {c}''')
print("\nFinal equation of the Best fit line is:")
if c>=0:
    print(f"y={m}x+{c}")
else:
    print(f"y={m}x{c}")
    
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
