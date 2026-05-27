""" 01 Реверс словаря

Напишите программу, которая
- меняет местами ключи и значения в словаре.
Если значения повторяются, добавьте их в список.

ВАЖНО: обратите внимание, что ключи становятся элементами списка,
       даже если значение ключа уникально!

Данные:
data = {"a": 1, "b": 2, "c": 1, "d": 3}
Пример вывода:
Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
"""
from operator import invert

data = {"a": 1, "b": 2, "c": 1, "d": 3}
# Вариант №1
inverted_dict = {}
for key, value in data.items():
    inverted_dict.setdefault(value, []).append(key)
print("Перевернутый словарь:", inverted_dict)

# Вариант №2
inverted_dict = {value: [key for key in data if data[key] == value] for value in data.values()}

print("Перевернутый словарь:", inverted_dict)