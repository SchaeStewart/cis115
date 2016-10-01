#Schaffer Stewart
#09/20/16
#Hourly Pay Program

#Input
employeeName = str(input("Please enter the employee's name\n"))#Employee Name
hoursWorked = float(input("Please enter the hours worked by the employee\n"))#Hours Worked
hourlyPay = float(input("Please enter the hourly pay of the employee\n"))#Hourly Pay

#Process
federalTaxRate = 0.2 #Set federal tax rate 
federalTaxRateAsPercent = federalTaxRate * 100 #Set the federal tax rate as a percentage
stateTaxRate = 0.09 #Set state tax rate 
stateTaxRateAsPercent = stateTaxRate * 100 #Set state tax rate as a percentage

grossPay = hoursWorked * hourlyPay #Set Gross pay to  hours worked * hourly pay
federalDeductions = grossPay * federalTaxRate #Set Federal deductions to Gross pay * federal tax rate 
federalDeductions = round(federalDeductions, 2) #Round the deductions to two decimal places 
stateDeductions = grossPay * stateTaxRate #Set State deductions to Gross pay * state tax rate 
stateDeductions = round(stateDeductions, 2) #Round the deductions to two decimal places
totalDeductions = federalDeductions + stateDeductions #Set Total deductions to State deductions + Federal deductions
netPay = grossPay - totalDeductions #Set Net pay to Gross pay - Total deductions

#Output
#Print name, hours worked, pay rate, gross pay, federal withholding, state withhodling, total deductions, and net pay
print("Name: " , employeeName)
print("Hours Worked: $" + str(hoursWorked))
print("Pay Rate: $" + str(hourlyPay))
print("Gross Pay: $" + str(grossPay))
print("Deductions:")
print("\tFederal Withholding(" + str(federalTaxRateAsPercent) + "%): $" + str(federalDeductions))
print("\tState Withholding(" + str(stateTaxRateAsPercent) + "%): $" + str(stateDeductions))
print("\tTotal Deductions: $" + str(totalDeductions))
print("Net Pay: $" + str(netPay))
