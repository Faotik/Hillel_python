###########################################
# Task 6
# Найти корни квадратного уравнения и вывести их на экран, если они есть.
# Если корней нет, то вывести сообщение об этом.
# Конкретное квадратное уравнение определяется коэффициентами a, b, c, которые вводит пользователь.

import math

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))

d = (b * b) - 4 * a * c

if d > 0:
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)
    print("Корни квадратного уравнения {} и {}".format(x1, x2))
if d == 0:
    x1 = -b/(2 * a)
    print("Корень квадратного уравнения {}".format(x1))
if d < 0:
    print("Корней нет")

input()
