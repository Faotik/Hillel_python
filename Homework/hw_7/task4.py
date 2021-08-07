######################################
# Task4
# Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном
# случае. 8 - YES, 3 - NO
######################################

def powerOfTwo(n, power=0):
    
    if 2 ** power == n:
        return "Yes"
    elif 2 ** power > n:
        return "No"
    power += 1
    return powerOfTwo(n, power)

num = int(input("Введите число: "))

print(powerOfTwo(num))

input()
