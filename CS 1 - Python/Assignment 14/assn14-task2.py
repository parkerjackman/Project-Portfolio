"""
Parker Jackman
Assignment 14
Task 2
"""

numList = []
done = False

while not done:
    num = input("Enter a number: ").strip()
    if num == "":
        break
    else:
        numList.append(int(num))

for i in range(1, len(numList)):
    currentNum = numList[i]
    j = i - 1
    while j >= 0 and numList[j] > currentNum:
        numList[j + 1] = numList[j]
        j -= 1

    numList[j + 1] = currentNum


print("# of values entered: " + str(len(numList)))
print("Min Value: " + str(numList.pop(0)))
print("Max Value: " + str(numList.pop()))
