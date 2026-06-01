"""Реализуйте функцию, которая принимает текст
и возвращает словарь с подсчётом количества каждой буквы,
игнорируя регистр.
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}"""

from collections import Counter

text = "Programming is fun!"
dict_text = Counter(text.lower().rstrip("!"))
print(dict(dict_text))
