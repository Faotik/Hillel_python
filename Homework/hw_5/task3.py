############################################
# Task3
# Напишите программу для поэлементного вычисления суммы заданных кортежей.
# Результатом должен быть кортеж.
############################################

tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)

list1 = list()

for i in range(len(tuple1)):
    list1.append(tuple1[i] + tuple2[i] + tuple3[i])

tuple4 = tuple(list1)

print(tuple4)

input()