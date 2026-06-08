""" 01 Объединение данных в строку

Напишите функцию, которая
- принимает список любых данных (строки, числа, списки, словари)
- и возвращает их строковое представление, объединённое через " | ".
  (т.е. объединяет результат в одну строку)

Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.


Данные:
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
Пример вывода:
42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
"""

from typing import List, Any


def str_return(sep: str, any_types: List[Any]) -> str:
    """
     This function converts a list of elements of various types
     into a string representation joined by the character;
     to achieve this, all list elements are first converted to strings,
      and then these strings are joined using the separator.

    :param sep: A string-type separator around which the string-based representations
                of any_types-list elements are grouped.
    :param any_types: A list consisting of elements of any type
    :return: A string representation of any_types-list elements separated by the character.
    """

    return sep.join([str(item) for item in data])


data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
print(str_return(" | ", data))
