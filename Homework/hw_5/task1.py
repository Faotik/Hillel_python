############################################
# Task1
# Напишите программу для преобразования списка в кортеж
############################################

import random

l = list()

for _ in range(10):
    l.append(random.randint(0, 20))

t = tuple(l)

print("List: ", l)
print("Tuple", t)

input()
