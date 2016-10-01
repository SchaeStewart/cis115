#Schaffer Stewart
#09/15/16
#Erorr Lab

#Kassler
#Feb 2012
#Section 1

#Receive the amount
amount = float(input("Enter the amount: "))# changed print to input

#Convert to cents
changedAmount = int(amount*100)

#Dollars
numDollars= changedAmount//100 #moved numDollars to before equals sign
changedAmount = changedAmount%100

#Quarters
numQuarters = changedAmount//25 #moved numQuarters to before equals sign. changed division (/) to int division (//)
changedAmount = changedAmount%25 #capitalized changedAmount. changed multiplication to modulus

#Dimes
numDimes = changedAmount//10 #moved numDimes to before equals sign
changedAmount = changedAmount%10

#Nickels
numNickels = changedAmount//5 #moved numNickels to before equals sign 
changedAmount = changedAmount%5 #lower cased changedAmount

#Pennies #made Pennies a comment
numPennies = changedAmount

#Output
print("For $", amount, "consists of: \n\t", numDollars, "dollars \n\t", numQuarters, "quarters \n\t", numDimes , "dimes \n\t", numNickels, "nickels \n\t", numPennies, "pennies") #added closing quote to pennies. Added , between numDimes and following string
