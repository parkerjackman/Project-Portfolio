"""
Parker Jackman
Assignment 6
task 2
"""

name = input("Enter employee's name: ")
numHours = eval(input("Enter number of hours worked in a week: "))
payRate = eval(input("Enter hourly pay rate: "))
fedTax = eval(input("Enter federal tax withholding rate (ex. 0.13): "))
stateTax = eval(input("Enter state tax withholding rate (ex. 0.06): "))

name = name.upper()
grossPay = numHours * payRate
fedWithholding = fedTax * grossPay
stateWithholding = stateTax * grossPay
totalDeduction = round(fedWithholding + stateWithholding, 2)
netPay = grossPay - totalDeduction

fedTax = round(fedTax * 100, 1)
fedTax = str(fedTax) + "%"
stateTax = round(stateTax * 100, 1)
stateTax = str(stateTax) + "%"

message = "\n"
message += format(name + " PAY INFORMATION", "^40s") + "\n"
message += "\n"
message += format("Pay", "^40s") + "\n"
message += format("Hours Worked:", ">28s")
message += format(numHours, ">12.0f") + "\n"
message += format("Pay Rate: $", ">30s")
message += format(payRate, ">10.2f") + "\n"
message += format("Gross Pay: $", ">30s")
message += format(grossPay, ">10.2f") + "\n"
message += "\n"
message += format("Deductions", "^40s") + "\n"
message += format("Federal Withholding (" + str(fedTax) + "): $", ">30s")
message += format(fedWithholding, ">10.2f") + "\n"
message += format("State Withholding (" + str(stateTax) + "): $", ">30s")
message += format(stateWithholding, ">10.2f") + "\n"
message += format("Total Deduction: $", ">30s")
message += format(totalDeduction, ">10.2f") + "\n"
message += "\n"
message += format("Net Pay: $", ">30s")
message += format(netPay, ">10.2f")

print(message)