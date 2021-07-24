############################################
# Task7
# Реализовать логику Union для двух списков (list),
# проверить работу алгоритма на set.union
############################################
import random

def Difference(set1, set2):
    differenceSet = set()

    for s1 in set1:
        if s1 not in set2:
            differenceSet.add(s1)
    return differenceSet
        

s1 = set()
s2 = set()

for _ in range(10):
    s1.add(random.randint(0, 20))
    s2.add(random.randint(0, 20))

print("A: ", s1)
print("B: ", s2)

print("Custom difference: ", Difference(s1, s2))
print("set.difference: ", set.difference(s1, s2))

input()
