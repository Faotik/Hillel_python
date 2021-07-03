###########################################
# Task 3
# Найти максимальное число из трех. Числа вводится с клавиатуры

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третие число: "))

if num1 > num2 and num1 > num3:
    maxNum = num1
elif num2 > num1 and num2 > num3:
    maxNum = num2
elif num3 > num1 and num3 > num2:
    maxNum = num3
print("Максимальное число {}".format(maxNum))

input()
