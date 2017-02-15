#Schaffer Stewart
#12/01/16
#Rock Paper Scissors Lab

import random

#Gets the computer's answer and return it as a string. If an error occurs, return false
def getComputerAnswer():
    rockPaperScissor = random.randint(1,3)

    if rockPaperScissor == 1:
        answer = "rock"
    elif rockPaperScissor == 2:
        answer = "paper"
    elif rockPaperScissor == 3:
        answer = "scissor"
    else: 
        answer = False
    return answer 

#Gets the user's answer and returns it as a lowercase string
def getUserAnswer():
    answer = input(str("Enter rock, paper, or scissors\n"))
    answer = answer.lower()
    if answer == "rock":
        return answer
    elif answer == "paper":
        return answer
    elif answer == "scissor":
        return answer
    else:
        print("Error please enter a valid choice")
        return getUserAnswer()

#Checks the computer's Answer against the user's answer to see who won
#Returns the result of the match as a string.
#Returns false if both answers are the same
def checkAnswer(userAnswer, computerAnswer):
    #Since the messages do not change if the computer or user wins,
    #define them as variables for less typing 
    rockMsg = "Rock smashes the scissors."
    paperMsg = "Paper covers rock."
    scissorMsg = "Scissors cut paper."

    if userAnswer == "rock" and computerAnswer == "scissor":
        result = rockMsg 
        result = result + " You win!"
        return result 
    elif userAnswer == "paper" and computerAnswer == "rock":
        result = paperMsg 
        result = result + " You win!"
        return result 
    elif userAnswer == "scissor" and computerAnswer == "paper":
        result = scissorMsg 
        result = result + " You win!"
        return result 
    elif computerAnswer == "rock" and userAnswer == "scissor":
        result = rockMsg 
        result = result + " The computer wins."
        return result 
    elif computerAnswer == "paper" and userAnswer == "rock":
        result = paperMsg 
        result = result + " The computer wins."
        return result 
    elif computerAnswer == "scissor" and userAnswer == "paper":
        result = scissorMsg 
        result = result + " The computer wins."
        return result 
    elif computerAnswer == userAnswer:
        print("You both chose " + userAnswer + " please try again")
        return False

def main():
    computerAnswer = getComputerAnswer()
    if computerAnswer == False:
        print("There's been an error, please try again")
        main()
    userAnswer = getUserAnswer()
    print("The computer chose: " + computerAnswer)
    result = checkAnswer(userAnswer, computerAnswer)
    if result == False:
        main()
    else:
        print(result)
main()
