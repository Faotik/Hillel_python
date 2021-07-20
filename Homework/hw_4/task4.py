###################################
# Task4
# Напишите программу для объединения следующих словарей для создания нового
###################################

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

dict4 = dict()

def addDict(newDict, addDict):
    for a in addDict:
        newDict[a] = addDict.get(a)
    return newDict

dict4 = addDict(dict4, dict1)
dict4 = addDict(dict4, dict2)
dict4 = addDict(dict4, dict3)

print(dict4)

input()
