###################################
# Task1
# Напишите программу Python, которая принимает слово от пользователя и переворачивает его
###################################

str = input("Введите строку: ")

InvertStr = ""

for i in range(1, len(str)+1):
    InvertStr += str[-i]

print("Перевернутая строка: {}".format(InvertStr))

input()
