#Schaffer Stewart
#10/05/16
#Simple addition game

import random
playing = True

while playing == True:
    #Define two random ints between 0-9
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    #Create answer
    answer = num1 + num2

    userGuess = int(input("What is "+str(num1)+" + "+str(num2) + "? "))

    if userGuess == answer:
        print("Correct")
    else:
        print("Please try again")


    playAgain = str.lower(str(input("Would you like to play again (y,n) ")))
    checkForPlayAgain = True

    while checkForPlayAgain == True:
        if playAgain == "y":
            playing=True
            checkForPlayAgain = False
        elif playAgain == "n":
            print("goodbye")
            checkForPlayAgain = False
            playing = False
        else:
            playAgain = str.lower(str(input("Would you like to play again (y,n) ")))
            str.lower(playAgain)
    
