##############################################
# Task1
# Напишите функцию calculations () так, чтобы она могла 
# принимать две переменные и вычислять их сложение и 
# вычитание. А также он должен возвращать как сложение, так 
# и вычитание за один вызов возврата.
##############################################

def calculation(a, b):
    sum = a + b
    subt = a - b

    return (sum, subt)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print(calculation(num1, num2))
print("Число {} результат сложения, а число {} результат вычитания".format(calculation(num1, num2)[0], calculation(num1, num2)[1]))

input()