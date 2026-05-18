""" 01 Проверка на подмножество

Напишите программу, которая
- проверяет, содержит ли первое множество все элементы второго множества.

Реализуйте решение несколькими способами.
(в том числе и способом, НЕ используящим возможности множеств).

Данные:
set1 = {1, 2, 3, 4}
set2 = {2, 3}
Пример вывода:
True
"""
set1 = {1, 2, 3, 4}
set2 = {2, 3}

# Варианты 1-6
print(set1.issuperset(set2))
print(set2.issubset(set1))
print(set1 == set1 | set2)
print(set2 == set1 & set2)
print(set() == set2 - set1)
print(set2 == set1 - (set1 - set2))

# Вариант 7
print(set2 == {item for item in set1 if item in set2})

# Вариант 8
set1_1 = set1.copy()
for item in set2:
    set1_1.add(item)
print(set1 == set1_1)

# Вариант 9
set1_1 = set(set1)
set1_1.update(set2)
print(set1_1 == set1)

# Вариант 10
res = True
for item in set2:
    if item not in set1:
        res = False
        break
print(res)

# Вариант 11 (можно было использовать копию set1, но так компактнее)
set2_2 = {x for x in set1 if x not in set2}
for item in set2_2:
    set1.discard(item)
print(set1 == set2)






