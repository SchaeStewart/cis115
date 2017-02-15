#Schaffer Stewart
#10.24.16
#Retail Price Calculator

#retail price = wholesale * markup 
markup = 2.5
import math

running = "y"
while running == "y":
    userInput = str(input("Input the wholesale cost (Type n to exit) "))
    if userInput.lower() == "n":
        print("Exiting! Thank you!")
        running = userInput
    elif math.isnan(userInput) == False:
        wholeSaleCost = float(userInput)
        if wholeSaleCost > 0:
            retailCost = wholeSaleCost + markup
            print("The retail cost is: " + str(retailCost))
        else:
            print("Invalid number, please try again:")
