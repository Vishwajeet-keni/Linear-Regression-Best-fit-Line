import matplotlib.pyplot as plt
from numpy import zeros 

n=int(input("Enter numbers if Data Points: "))

x=zeros(n,float)     # array to store x
xSq=zeros(n,float)   # array to store x square
y=zeros(n,float)     # array to store y
xy=zeros(n,float)    # array to store x.y


i=0
while i<n:                                # loop to collect x co-ordinat of Data points and store in array (x)
    x[i]=float(input(f"Enter x{i+1}: "))  
    i+=1
Sum_X=sum(x)     # Sums all the valus stored in array (x)

i=0
while i<n:                                # loop to collect y co-ordinat of Data points and store in array (y)
    y[i]=float(input(f"Enter y{i+1}: "))
    i+=1
Sum_Y=sum(y)     # Sums all the valus stored in array (y)

i=0
while i<n:             # loop which square the values stored in x and store in (xSq)
    xSq[i]=x[i]**2
    i+=1
Sum_Xsq=sum(xSq)     # Sums all the valus stored in array (xSq)
      
i=0
while i<n:            # loop which multiplies the value stored in x & y then save them in array(xy)
    xy[i]=x[i]*y[i]
    i+=1
Sum_XY=sum(xy)     # Sums all the valus stored in array (xy)


m=(n*Sum_XY - Sum_X*Sum_Y)/(n*Sum_Xsq - (Sum_X)**2)     # Calculating Slope
c=(Sum_Y - (m*Sum_X))/n     #Calculating Intercept

print("Sum_X: ",Sum_X)
print("Sum_Y: ",Sum_Y)
print("Sum_Xsq: ",Sum_Xsq)
print("Sum_XY: ",Sum_XY) 
print("Slope m= ", m)
print("Intercept c= ", c)
print("Final equation of the Best fit line is:")
if c>=0:
    print(f"y={m}x+{c}")
else:
    print(f"y={m}x {c}")

plt.scatter(x,y,color='blue',marker="o",label="Data Points")
y_pred=m*x+c
plt.plot(x,y_pred,color='red', label="Best Fit Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.title("Linear Regression: Best fit Line")
plt.legend()
plt.grid(linestyle=":")
plt.show()
