#Schaffer Stewart
#10/04/16
#Eightball Simulator

import random
programRunning = True

while programRunning:
    #Ask for input as a string
    question = str(input("Ask your question "))
    randNum = random.randint(1,6)
    if randNum == 1:
        print("Yes")
    elif randNum == 2:
        print("Out look is good")
    elif randNum == 3:
        print("Better not tell now")
    elif randNum == 4:
        print("Ask again later")
    elif randNum == 5:
        print("Don't count on it")
    elif randNum == 6:
        print("Out look not good")
    else:
        print("Error, please try again")
        
    playAgain = str(input("Would you like to play again (y, n) "))
    playAgain.lower()
    checkPlayAgain = True
    while checkPlayAgain == True:
        if playAgain == "y":
            programRunning = True
            checkPlayAgain = False
        elif playAgain == "n":
            programRunning = False
            checkPlayAgain = False
        else:
            checkPlayAgain = True


#if num ==1
#out Yes
#elif num ==2 
#out Outlook good
#elif num ==3
#out better not tell now
#elif == 4 
#Ask again later
#elif ==5
#Don't count on it
#elif == 6
#Out Out look not good
#else
#out error, please try again
