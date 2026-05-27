""" 02 Счётчик букв в словах

Напишите программу, которая
- подсчитывает количество каждой буквы в заданных словах
- и создаёт словарь, где
        ключи — это слова,
        а значения — это ещё один словарь, где
                ключ - это буква,
                а значение - число повторений этой буквы в слове.
Данные:
words = ["anna", "bennet", "john"]

Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}

"""
words = ["anna", "bennet", "john"]

# Вариант №1
dict_words = {word: {char: word.count(char) for char in word} for word in words}

print(dict_words)

# Вариант №2
dict_words = {}
for word in words:
    d = {}
    for char in word:
        d[char] = d.get(char, 0) + 1
    dict_words[word] = d
print(dict_words)
