###########################################
# Task 4
# Определить високосный год или нет.Число вводится с клавиатуры

year = int(input("Введите год: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("{} высокосный год".format(year))
        else:
            print("{} не высокосный год".format(year))
    else:
        print("{} высокосный год".format(year))
else: 
    print("{} не высокосный год".format(year))

input()
