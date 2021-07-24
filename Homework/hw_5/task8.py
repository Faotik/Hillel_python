############################################
# Task7
# Реализовать логику Union для двух списков (list), 
# проверить работу алгоритма на set.union
############################################

import random

def Union(set1, set2):
    unionSet = set()

    for s in set1:
        unionSet.add(s)
    for s in set2:
        unionSet.add(s)
    return unionSet

s1 = set()
s2 = set()

for _ in range(10):
    s1.add(random.randint(0, 20))
    s2.add(random.randint(0, 20))


print("A: ", s1)
print("B: ", s2)

print("Custom union: ", Union(s1, s2))
print("set.union: ", set.union(s1, s2))

input()
