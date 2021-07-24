############################################
# Task2
# Напишите программу для замены последнего значения кортежей в списке
############################################

startList = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

print("Start list: ", startList)

tempList = list()

for i in range(len(startList)):
    for q in range(len(startList[i])):
        tempList = list(startList[i])
        tempList[-1] = 100
        tempTuple = tuple(tempList)
        startList[i] = tempTuple

print("Output list: ", startList)

input()
