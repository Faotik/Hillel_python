###################################
# Task2
# Даны два целых числа A и В. 
# Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания если A > B
###################################

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a < b:
    for i in range(a, b + 1):
        print(i)
if a > b:
    for i in range(a, b - 1, - 1):
        print(i)

input()