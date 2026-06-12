""" 02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""
def sum_digits_non_tail(lst: list[int | float | list]) -> int | float:
    sum_num = 0
    for item in lst:
        if isinstance(item, list):
            sum_num += sum_digits_non_tail(item)
        else:
            sum_num += item
    return sum_num

def sum_digits_tail(lst, acc=0):
    for item in lst:
        if isinstance(item, list):
            acc = sum_digits_tail(item, acc)
        else:
            acc += item
    return acc


nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

print(sum_digits_tail(nested_numbers))       # 28
print(sum_digits_non_tail(nested_numbers))   # 28