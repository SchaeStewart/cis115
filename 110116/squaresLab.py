#Schaffer Stewart
#11/01/16
#Squares Lab


highestVal = int(input("What is the highest value you wish to find the square for: "))

print("Number\t Square")
for i in range(1, highestVal+1):
    print(str(i) +"\t " + str(i*i))
