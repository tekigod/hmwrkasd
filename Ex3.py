# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random

l1st = int(input("Введите размер списка: "))

randomList = []
unique = []

for i in range(l1st):
    randomList.append(random.randint(0, 9))
print(f"Заданный список: {randomList}")

for asd in randomList:
    count = 0
    for qwe in randomList:
        if asd == qwe:
            count += 1
    if count == 1:
        unique.append(asd)
print(f"Уникальные элементы в списке: {unique}")