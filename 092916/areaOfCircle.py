#Schaffer Stewart, Alan Skonieczny, Nathan Dabbs
#09/29/16
#Radius Conditionals
import math

programRunning = True
while programRunning == True:
    radius = float(input("Please enter the radius "))
    if radius > 0:
        area = math.pi * radius**2
        print("The area is: " , area)
        programRunning = False
    else:
        print("The radius is not a positive number")
        
    
