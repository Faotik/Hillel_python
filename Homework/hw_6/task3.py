#######################################
# Task3
# Напишите функцию func () так, чтобы она могла принимать 
# аргументы переменной длины и выводить все значения 
# аргументов с индексом аргумента.
#######################################

import random

def func(*args):
    i = 0
    for a in args:
        print("Аргумент: {}, индекс аргумента {}".format(a, i))
        i += 1

#I dont know how i can edit argument without editing it in code
func(5, 3, "arg1", "arg2", 3.4)

input()