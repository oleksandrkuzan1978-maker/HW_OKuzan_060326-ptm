""" 01 Оценки текстом

Напишите программу, которая
- преобразует список оценок по системе от 1 до 5 в текстовое представление.

Нужно сохранить в списках числовой результат и текстовое представление.
 Где, 5 — "отлично", 3-4 — "хорошо", а 2 и ниже — "неудовлетворительно".
Данные:
grades = [5, 3, 4, 2, 1, 5, 3]

Пример вывода:
[[5, 'отлично'], [3, 'хорошо'], [4, 'хорошо'], [2, 'неудовлетворительно'], [1, 'неудовлетворительно'], [5, 'отлично'], [3, 'хорошо']]

"""
# ВАРИАНТ №1
grades = [5, 3, 4, 2, 1, 5, 3]
texts = [[grade] for grade in grades]
for i, grade in enumerate(grades):
    if grade == 5:
        texts[i].append("отлично")
    elif grade >= 3:
        texts[i].append("хорошо")
    else:
        texts[i].append("неудовлетворительно")
print(texts)

# ВАРИАНТ №2
# grades = [5, 3, 4, 2, 1, 5, 3]
#
# texts = []
#
# for grade in grades:
#     if grade == 5:
#         texts.append("отлично")
#     elif grade >= 3:
#         texts.append("хорошо")
#     else:
#         texts.append("неудовлетворительно")
#
# zipped = zip(grades, texts)
#
# print([list(zipp) for zipp in zipped])