#Kassler
#Sept 2011
#Section 1 and 2 #commented "Section 1 and 2"
#My program won't work :(


#input
name = str(input("Please enter your name ")) #replaced print, with str(input())

print("Hello " , name)  #checking to see if it works.  #Added string concatenation

year = int(input("What year were you born? ")) #added closing ". added int
#process
age = 2016 - year #changed 2011 to 2016. changed to 2016 - year
print("Wow, you are, " ,  age) #changed Age to age. Added string concatenation
print("I wonder if you qualify for a senior discount...")
if age > 55:
    print("you qualify") #added print()
else: #added colon
    print("you don\'t qualify") #added quotes and esacped the '
print("Have a good day") #changed Print to print. 
