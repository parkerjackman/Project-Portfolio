

class Account:
    def __init__(self, id = 0, balance = 100.00, annualInterestRate = 0.0):
        self.__id = format(id, "d")
        self.__balance = format(balance, ".2f")
        self.__annualInterestRate = format(annualInterestRate, "f")

    def getMonthlyInterestRate(self, annualInterestRate):
        monthlyInterestRate = format(annualInterestRate / 12, ".1f")
        return monthlyInterestRate

    def getMonthlyInterest(self, balance, annualInterestRate):
        monthlyInterest = format(balance * ((annualInterestRate / 100) / 12), ".2f")
        return monthlyInterest

    def withdraw(self, balance, amount):
        return balance - amount

    def deposit(self, balance, amount):
        return balance + amount




