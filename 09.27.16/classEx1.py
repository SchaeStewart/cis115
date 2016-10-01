#Schaffer
import math

area = float(input("Enter the area: " ))
if area >= 0:
    radius = math.sqrt(area/math.pi)
    print("The radius is " , radius)
else:
    print("Error: the area musy be a positive number")
