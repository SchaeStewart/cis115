#Schaffer Stewart
#10/25/16
#Retail Calculator

markup = 2.5
running = True
while running:
    wholesale = float(input("Whole sale price "))
    if wholesale <= 0:
        print("Please enter a positive number")
    else:
        retail = wholesale * markup
        print("The retail price is: " + str(retail))
    again = True
    while again:
        userInput = str(input("Check another price? (y/n) "))
        if userInput.lower() == 'n':
            running = False
            again = False
            print("Goodbye")
        elif userInput.lower() == 'y':
            again = False
        else:
            print("Error")
