"""
Parker Jackman
Assignment 8
Task 1
"""

import timeit

start = timeit.default_timer()

i = 1
LOOP_COUNT = 10000
inner_loop = 0
while i < LOOP_COUNT:
    sum = 0
    test_number = int(i / 2 + 1)
    for j in range(1, test_number):
        inner_loop += 1
        if i % j == 0:
            sum += j
        else:
            continue
    if sum == i:
        print(i, "is a perfect number")
    i += 1

print("The inner loop ran", inner_loop, "iterations.")

stop = timeit.default_timer()
execution_time = stop - start
print("The program took", execution_time, "seconds to execute")