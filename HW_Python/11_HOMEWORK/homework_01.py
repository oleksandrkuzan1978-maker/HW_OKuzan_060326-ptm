""" 01 Звёздочки вместо чисел

Напишите программу, которая заменяет все цифры в строке на звёздочки *.

text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""
# ЗАДАНИЕ №1
# Вариант №1
text = "My number is 123-456-789"
text1 = ""
print("Строка:", text)
for char in text:
    if char.isdigit():
        text1 += "*"
    else:
        text1 += char
print("Результат:", text1)

# Вариант №2
text = "My number is 123-456-789"
print("Строка:", text)
text = list(text)
for i in range(len(text)):
    if text[i].isdigit():
        text[i] = "*"
print("Результат:", "".join(text))
