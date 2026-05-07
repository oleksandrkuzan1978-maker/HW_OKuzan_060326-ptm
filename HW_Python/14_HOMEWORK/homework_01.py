""" 01 Число в конце

Напишите программу, которая
- создает новый список.
В него необходимо добавить только те строки из исходного списка,
в которых цифры находятся только в конце.

Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']
"""

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new = []

for item in strings:
    item1 = item.rstrip("0123456789")
    if item1.isalpha():
        new.append(item)

print("Строки с цифрами только в конце:", new)
