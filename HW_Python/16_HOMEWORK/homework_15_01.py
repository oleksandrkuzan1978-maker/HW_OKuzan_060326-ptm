""" 01. Одно слово

Напишите программу, которая
- обрабатывает список из строк
- и удаляет все строки, содержащие более одного слова,
- а также преобразует оставшиеся строки к нижнему регистру.

ВАЖНО: НЕ создать новый список, а УДАЛИТЬ лишние элементы из существующего!

Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

# Вариант №1
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

for i, string in enumerate(text_list[:]):
    text_list.remove(string)
    if string.find(" ") == -1:
        text_list.insert(i, string.lower())

print(text_list)

# Вариант №2
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# l = len(text_list)
# i=0
# while i < l:
#     if text_list[i].find(" ") != -1:
#         text_list.remove(text_list[i])
#         l -= 1
#     else:
#         text_list[i] = text_list[i].lower()
#         i +=1
# print(text_list)