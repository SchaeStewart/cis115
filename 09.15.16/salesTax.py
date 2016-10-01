#Schaffer Stewart
#09/15/16
#Sales Tax Calculator

#Input
subtotal = float(input("Please enter your subtotal\n"))#Get users subtotal

#Process
tax = 0.075 #create variable for tax amount
taxAmount = tax * subtotal #calculate the tax they will pay and save it to a variable
taxAmount = round(taxAmount, 2)#round taxAmount to 2 decimal places
total = taxAmount + subtotal #calculate total and save it to variable

#Output
print("The tax amount is:\n$",taxAmount) #Print taxAmount
print("The total amount is:\n$", total) #print total
