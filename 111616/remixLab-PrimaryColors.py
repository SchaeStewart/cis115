#Schaffer Stewart
#11/16/16
#Remix Lab - Color Mixer

# colorMixer function
# Takes the input of two primary colors and prints the result
# Else it prints an error

def colorMixer(color1, color2):
    color1 = color1.lower()
    color2 = color2.lower()

    if color1 == 'red' and color2 == 'blue' or color2 == 'red' and color1 == 'blue':
        print('Purple')
    elif color1 == 'red' and color2 == 'yellow' or color1 == 'yellow' and color2 == 'red':
        print('Orange')
    elif color1 == 'blue' and color2 == 'yellow' or color1 == 'blue' and color2 == 'yellow' and color == 'blue':
        print('Green')
    else:
        print('Please enter a valid primary color')

def mixAgain():
    again = str(input('Would you like to mix another color? (y/n) '))
    again = again.lower()
    if again ==  'y':
        return  True 
    elif again == 'n':
        return False
    else:
        print('Error')
        mixAgain()

programRunning = True
while programRunning == True:
    #Get colors from user
    color1 = str(input('Please enter a primary color '))
    color2 = str(input('Please enter another primary color ')) 

    #Pass colors to colorMixer function
    colorMixer(color1, color2)

    #Check if the user wants to mix colors again
    programRunning = mixAgain()
