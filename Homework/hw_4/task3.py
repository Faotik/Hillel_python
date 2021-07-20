###################################
# Task3
# Напишите программу, которая находит разницу между двумя списками и сохраняет ее в новый список.
# Вывести результат на экран.
###################################

import random

arr = list()
arr2 = list()

for num in range(5):
    arr.append(random.randint(0, 10))
    arr2.append(random.randint(0, 10))

newArr = list()

for a in arr:
    if a not in arr2:
        newArr.append(a)
for a in arr2:
    if a not in arr and a not in newArr:
        newArr.append(a)


print("Первый список 1: ", arr)
print("Второй список 2: ", arr2)
print("Разница в списках: ", newArr)

input()
