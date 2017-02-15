#Schaffer Stewart
#12/08/16
#Review Ex. 1

def calculateDiscount(price):
    if price == 100:
        return 100 + 20
    elif price == 50:
        return 50 + 10
    elif price == 25:
        return price + 5
    elif price == 5 or price == 10:
        return price
    else:
        return "Error"

def getAmount():
    amount = int(input("Please enter the amount you would like on your card\n(5, 10, 25, 50, 100) "))
    return amount

def returnUpdatedAmount():
    amount = getAmount()
    updatedAmount = calculateDiscount(amount)
    return updatedAmount
    #print("Congrats! You know have $" + str(totalMoneyOnCard) + " on your card")

returnUpdatedAmount()
