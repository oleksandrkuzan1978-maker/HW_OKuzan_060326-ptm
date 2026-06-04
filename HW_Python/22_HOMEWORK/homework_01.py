""" 01 Выбор заказов

У вас есть список заказов.
Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
- Отбирает заказы дороже 500.
- Создаёт список названий отобранных продуктов в алфавитном порядке.
- Возвращает итоговый список названий.

Данные:
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

Пример вывода:
['Chair', 'Laptop']

"""
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
sample = ['Chair', 'Laptop']


# Вариант №1
def select_expensive_orders(ords):
    # Отбор только тех элементов(словарей) в списке, у которых значение ключа "price" > 500
    expens = filter(lambda order: order["price"] > 500, ords)
    # Из получившегося итератора формируем коллекцию значений словарей по ключу "product"
    prod_expens = map(lambda order: order["product"], expens)
    # Создание отсортированного списка и возвращение его как результата функции
    return sorted(prod_expens)

result = select_expensive_orders(orders)
print(result)
print(result == sample)


# Вариант №2
def select_expensive_orders(ords):
    # Через list comprehension создаем отсортированный по названию
    # список из наименований продуктов у которых цена > 500
    return sorted(order["product"]
                  for order in ords
                  if order["price"] > 500)

result = select_expensive_orders(orders)
print(result)
print(result == sample)


# Вариант №3 (если не привязываться к названиям ключей)
def select_expensive_orders(ords):
    # Отбор только тех элементов(словарей) в списке, у которых значение ключа "price" > 500
    expens = filter(lambda order: list(order.values())[1] > 500, ords)
    # Из получившейся коллекции словарей формируем коллекцию их значений по ключу "product"
    prod_expens = map(lambda order: list(order.values())[0], expens)
    return sorted(prod_expens)
result = select_expensive_orders(orders)
print(result)
print(result == sample)