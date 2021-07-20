###################################
# Task1
# Напишите программу, которая удаляет дубликаты элементов из списка.
###################################

import random

arr = list()

for num in range(10):
    arr.append(random.randint(0, 20))

print("Первоначальный список: ", arr)

newArr = list()

for a in arr:
    if(a not in newArr):
        newArr.append(a)

print("Новый список: ",newArr)

input()
