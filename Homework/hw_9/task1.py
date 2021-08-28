#####################################################
# Task1
# Напишите функцию для создания файла и записи в него случайных чисел,
# каждое число записывается в файл через пробел, но не больше 10ти чисел в
# строку. Всего случайных чисел должно быть 1000
#
# Напишите другую функцию, которая считывает первый файл и возводит
# каждое число в квадрат. Каждое полученное число должно быть дозаписано
# в исходный файл в таком же формате.
#####################################################

import random

def writeRandomNumberInFile(countOfNumber):
    file = open("fileWithNumber.txt", "w")

    numberInLine = 0

    for i in range(countOfNumber):
        if (numberInLine >= 10):
            file.write("\n")
            numberInLine = 0

        file.write(str(random.randint(0, 100)) + " ")
        numberInLine += 1

    file.write("\n")
    file.close()


def writeSquareOfNumberInFile(countOfLine):
    file = open("fileWithNumber.txt", "r+")
    lines = file.readlines()
    cursPos = 0
    for line in lines:
        numbers = line.split()
        cursPos += len(line)
        for n in numbers:
            file.seek(0, 2)
            file.write(str(int(n) ** 2) + " ")
        file.write("\n")
        file.seek(cursPos)
    file.seek(0, 2)
    file.close()

writeRandomNumberInFile(1000)
writeSquareOfNumberInFile(100)
