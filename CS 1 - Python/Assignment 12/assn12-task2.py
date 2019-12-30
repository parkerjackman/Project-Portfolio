"""
Parker Jackman
Assignment 12
This program tests if a password is valid
"""

from password import Password

p = Password()

done = False

while not done:
    password = input("Enter Password: ")

    p.setPassword(password)

    if p.isValid():
        print("Valid Password!")

    else:
        print("Invalid Password.")
        print(p.getErrorMessage())

    again = input("Do you want to enter another password? (Y or N) ").upper()
    if again == "Y":
        continue
    else:
        done = True
