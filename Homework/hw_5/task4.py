############################################
# Task4
# Напишите программу, которая проверяет, присутствует ли А внаборе или нет. 
# А вводится с клавиатуры
############################################

import random

s1 = set()

for _ in range(10):
    s1.add(random.randint(0, 20))

print(s1)

A = int(input("Enter A: "))

aInSet = False

for s in s1:
    if A == s:
        aInSet = True
        break

if aInSet:
    print("Number A is in the set")
else:
    print("Number A is not in the set")

input()