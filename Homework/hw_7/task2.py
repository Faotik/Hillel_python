######################################
# Task2
# Напишите рекурсивную функцию для вычисления числа
# Фибоначи
######################################

def Fibonacc(count = 10, lastnum = 0, num = 1):
    print(lastnum, end=", ")
    count -= 1
    if count <= 0:
        return
    Fibonacc(count, num, lastnum + num )

count = int(input("Введите длину последовательности: "))
Fibonacc(count)

input()