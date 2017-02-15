#Schaffer Stewart
#10.27.26
#Dice Roll Program

import random 
counter = 0
rolling = True
while rolling:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    counter += 1
    if dice1 + dice2 == 7:
        print("It took " + str(counter) + " rolls to get 7")
        rolling = False
    else:
        print("dice 1 = " + str(dice1) + " dice 2 = " + str(dice2))
