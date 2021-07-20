###################################
# Task2
# Напишите программу, которая копирует список
###################################

import random

arr = list()

for num in range(10):
    arr.append(random.randint(0, 20))

arr2 = list()

for a in arr:
    arr2.append(a)

print("Первый список 1: ", arr)
print("Второй список 2: ", arr2)

input()
