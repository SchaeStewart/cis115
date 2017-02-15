#Kassler
#Nov 6
#Section 3
#Distance


hours = int(input("Enter the total number of hours: "))
mph = int(input("Enter your miles per hour (mph): "))
minutes = hours * 60

print("\nDistance \t Minutes")

for x in range(0, minutes+1, 15):
    d = mph * (x/60)
    print(d, "miles \t", x)
