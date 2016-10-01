#Schaffer Stewart, Alan Skonieczny, Nathan Dabbs
#09/29/16
#Primary color mixer

programRunning = False

while programRunning == False:
    color1 = str(input("Please enter a primary color (red, yellow, or blue) "))
    color2 = str(input("Please enter another primary color: "))
    #Make strings lowercase to avoid inpit issues
    color1 = color1.lower()
    color2 = color2.lower()
    if color1 == "red" and color2 == "blue" or color2 == "red" and color1 =="blue":
        print("Purple")
        programRunning = True
    elif color1 == "red" and color2 == "yellow" or color1 == "yellow" and color2 == "red":
        print("Orange")
        programRunning = True
    elif color1 == "blue" and color2 == "yellow" or color1 == "yellow" and color2 == "blue":
        print("Green")
        programRunning = True
    else:
        print("Please enter a valid primary color")

print("Thanks!")
