from account import Account

correct = False

while not correct:
    id = eval(input("Enter ID#: "))
    balance = eval(input("Enter starting balance: "))
    annualInterestRate = eval(input("Enter starting annual interest rate: "))
    if id < 0:
        print("Invalid ID input. Please try again")
    elif balance < 0.00:
        print("Invalid Balance input. Please try again")
    elif annualInterestRate < 0 or annualInterestRate > 10:
        print("Invalid Annual Interest Rate input. Please try again")
    else:
        correct = True

done = False

while not done:
    account = Account()

    print("Choose an option:")
    print("(1): Display ID")
    print("(2): Display Balance")
    print("(3): Display Annual Interest Rate")
    print("(4): Display Monthly Interest Rate")
    print("(5): Display Monthly Interest")
    print("(6): Withdraw Money")
    print("(7): Deposit Money")
    print("(8): Exit")

    choice = eval(input("What do you want to do? "))

    if choice == 1:
        print("")
        print("ID:", id)
        print("")
        print("Modify ID?")
        print("(1): Modify ID")
        print("(2): Leave it the same")
        modify = eval(input("What do you want to do? "))
        if modify == 1:
            id = format(eval(input("What is your new ID? ")), "d")
        else:
            continue

    elif choice == 2:
        print("")
        print("Balance: $" + str(balance))
        print("")
        print("Modify Balance?")
        print("(1): Modify Balance")
        print("(2): Leave it the same")
        modify = eval(input("What do you want to do? "))
        if modify == 1:
            balance = format(eval(input("What is your new Balance? ")), ".2f")
        else:
            continue

    elif choice == 3:
        print("")
        print("Annual Interest Rate: " + str(annualInterestRate) + "%")
        print("")
        print("Modify Annual Interest Rate?")
        print("(1): Modify Annual Interest Rate")
        print("(2): Leave it the same")
        modify = eval(input("What do you want to do? "))
        if modify == 1:
            annualInterestRate = format(eval(input("What is your new Annual Interest rate? ")), ".2f")
        else:
            continue

    elif choice == 4:
        print("")
        print("Monthly Interest Rate: " + str(account.getMonthlyInterestRate(annualInterestRate)) + "%")

    elif choice == 5:
        print("")
        print("Monthly Interest: " + str(account.getMonthlyInterest(balance, annualInterestRate)))

    elif choice == 6:
        print("")
        amountOut = eval(input("How much do you want to withdraw? "))
        balance = account.withdraw(balance, amountOut)
        print("Your new balance is $" + str(balance))

    elif choice == 7:
        print("")
        amountIn = eval(input("How much do you want to deposit? "))
        balance = account.deposit(balance, amountIn)
        print("Your new balance is $" + str(balance))

    elif choice == 8:
        done = True

    else:
        print("")
        print("Invalid input. Please try again")

print("Have a nice day!")