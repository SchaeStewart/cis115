#Basic loop

#repeat="y"
#while repeat == "y":
#    <statement>
#    <statement>
#    repeat = str(input("Continue: y/n"))
#<next block of code>

#sentinel value for ending loops
t = 0
w = float(input("Enter weight: "))
while w!=0:
    t+=w
    w=float(input("Enter wieghtL :"))
print(t)

