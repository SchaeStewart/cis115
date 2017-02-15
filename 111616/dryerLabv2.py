#Schaffer Stewart
#11/16/16
#Dryer Lab

def printStep(stepNum, message):
    input("Press Enter to see Step " + str(stepNum) +"\n")
    print("Step " + str(stepNum) + ": " + message)


def main():
    print("This progrma tells you how to disassemble an ACME laundry dryer.\nThere are four steps in the process.")
    printStep(1, "Unplug the dryer and move it away from the wall.")
    printStep(2, "Remove the six screws from the back of the dryer.")
    printStep(3, "Remove the back panel from the dryer.")
    printStep(4, "Pull the top of the dryer straight up.")


main()
