#Schaffer Stewart
#10.24.16
#Retail Price Calculator
import math
markup = 2.5
running = True
while running == True:
    userInput = input("Enter the wholesale cost or press \'n\' to exit ")
    if type(userInput) == str and userInput.lower() == 'n':
        print("goodbye")
        running = False 
    elif type(userInput) == str: 
        if int(userInput) == int:
            print("fucking work")

    if type(userInput) == float and userInput <= 0 or type(userInput) == int and userInput <= 0:
        print("ERROR")
    elif type(userInput) == float or type(userInput) == int:
        userInput = float(userInput)
        retailCost = markup * userInput
        print("The retail cost is: " + str(retailCost))
