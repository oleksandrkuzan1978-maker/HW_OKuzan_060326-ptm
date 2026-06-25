""" 03 Объединение списков продуктов

Напишите функцию, которая
- принимает несколько (много) списков с названиями продуктов
- и возвращает генератор, содержащий все продукты в нижнем регистре.

Выведите содержимое генератора.

Данные:
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""

from itertools import chain

fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Tomato", "Cucumber"]
dairy = ["Milk", "Cheese", "Yogurt"]


def gen(*args):

    return (prod.lower() for prod in chain(*args))

chain_goods = gen(fruits, vegetables, dairy)

for item in chain_goods:
    print(item)
