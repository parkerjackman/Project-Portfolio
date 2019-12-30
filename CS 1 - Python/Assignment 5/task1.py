"""
Parker Jackman
Assignment 5
Task 1
"""

print("This program calculates future investment values.")

investmentAmount = eval(input("Enter investment amount: "))
annualInterest = eval(input("Enter annual interest rate (eg 8.45): ")) / 100
numYears = eval(input("Enter number of years: "))

monthlyInterest = annualInterest / 12
numMonths = numYears * 12

futureInvestmentValue = investmentAmount * (1 + monthlyInterest)**numMonths

futureInvestmentValue = round(futureInvestmentValue, 2)

print("Accumulated value is", futureInvestmentValue)



