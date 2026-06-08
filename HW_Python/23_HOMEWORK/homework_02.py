""" 02 Сумма вложенных чисел

Напишите функцию, которая
- принимает список словарей, где каждый словарь содержит
    - имя пользователя
    - и список баллов.
- Функция должна вернуть сумму всех чисел.
- Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.

Данные:
data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

Пример вывода:
Итоговый балл: 156
"""
from functools import reduce


def sum_nested_scores(param: Dict) -> int:
    """
     The function sums all the numbers found in the values сorresponding
     to the second key across all dictionaries in the list "param".

    :param param: A list of dictionaries. The keys of these dictionaries are strings;
                  the value associated with the first key is a string,
                  and the value associated with the second key is an integer.

    :return: The sum of all numbers in the list of dictionaries "param".
    """
    # Создаем список, состоящий из сумм всех баллов каждого пользователя
    sum_score = [sum(user["scores"]) for user in param]
    # Суммируем все элементы списка sum_score
    return reduce(lambda v, x: v + x, sum_score)


data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

print(f"Итоговый балл: {sum_nested_scores(data)}")
