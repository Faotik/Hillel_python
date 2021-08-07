######################################
# Task3
# Напишите функцию для умножения всех чисел в списке.
# Рекурсивно
######################################

import random

def multpipleList(list2mult, i = 0):
    if(i == len(list2mult)):
        return 1
    i += 1
    return list2mult[i - 1] * multpipleList(list2mult, i)

l = list()

for _ in range(5):
    l.append(random.randint(1, 20))

print(l)
print(multpipleList(l))

input()