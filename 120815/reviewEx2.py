#Schaffer Stewart
#12/08/16
#Review Ex2 

def getGrade():
    grade = float(input("Enter the grade "))
    return grade
def addMoreGrades():
    addMoreGrades = input("Would you like to add another grade (y/n)")
    addMoreGrades = addMoreGrades.lower()
    if addMoreGrades == 'y':
        getGrade()
    elif addMoreGrades == 'n':
        return
    else:
        print("Error")
        addMoreGrades()


def enterGrades():
    grades = []
    grades.insert(0, getGrade())
   addMoreGrades()

    #get grade and add to list
    #ask if you wants to add more items
    
