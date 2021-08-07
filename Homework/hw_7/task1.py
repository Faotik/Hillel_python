######################################
# Task1
# Дано натуральное число N. Вычислите сумму его цифр.
# Напишите рекурсивную функцию
######################################

def numSum(number):
    if number == 0:
        return number
    return number % 10 + numSum(int(number / 10))

num = int(input("Введите число: "))
print("Сумма его цифр: ", numSum(num))

input()