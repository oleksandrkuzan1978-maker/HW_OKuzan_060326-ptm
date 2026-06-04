""" 02 Статистика продаж

Дан двумерный массив продаж (список тюплов): (товар, количество, цена).

Напишите программу, которая:
- Вычисляет общую выручку для каждого товара.
- Возвращает словарь с товарами {товар: выручка},
    отсортированный по убыванию выручки.

Данные:
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

Пример вывода:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

"""
# Вариант №1
from fontTools.ttx import process

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

sample = {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}


def calculate_sales(sales):
    # Создаем объект-представление состоящий из кортежей ("имя продукта", общая выручка от продукта)
    # t[0], t[1], t[2] - элементы каждого тюпла (товар, количество, цена) в списке sales
    revenue = dict(map(lambda t: (t[0], t[1] * t[2]), sales)).items()
    # Cортировка кортежей в revenue по убыванию величины общей выручки item[1]
    # создание словаря из отсортированного объекта revenue и возвращение как результата ф-ции
    return dict(sorted(revenue, key=lambda item: -item[1]))


result = calculate_sales(sales)
print(result)
print(str(result) == str(sample))


# Вариант №2
def calculate_sales(sales):
    # Создаем новый словарь состоящий из пар "имя продукта": общая выручка от продукта
    revenue = {product: quantity * price
               for product, quantity, price in sales}
    # Cортировка пар item словаря revenue по убыванию величины общей выручки item[1]
    # и его возвращение как результата ф-ции
    return dict(sorted(revenue.items(), key=lambda item: -item[1]))


result = calculate_sales(sales)
print(result)
print(str(result) == str(sample))
