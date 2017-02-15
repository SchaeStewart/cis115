#Schaffer Stewart
#10.24.16
#Retail Price Calculator
import math
markup = 2.5
running = True
while running == True:
    #first input
    userInput = float(input("Enter the wholesale cost: "))
    checkForBad = True
    while checkForBad == True:
        if userInput <= 0:
            print("Please use a positive number")
        else:
            checkForBad = False
    retailCost = markup * userInput
    print("Retail cost is: " + str(retailCost))
    checkAgain = True
    while checkAgain == True:
        userCheck = str(input("Check another item? (y/n)"))
        if userCheck == "y":
            checkAgain = False
            running = True
        elif

