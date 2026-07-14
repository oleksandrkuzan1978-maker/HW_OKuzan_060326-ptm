""" 01 Среднее время выполнения

Создайте декоратор measure_time, который
- измеряет и выводит среднее время выполнения функции за 5 вызовов.

Функция может быть любой:
    например, сортировка списка, чтение из файла или расчёты.

Пример применения:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 5 вызовов: 0.21 секунд
Результат: 49999995000000

"""

import time
from typing import Callable


def measure_time(func: Callable) -> Callable:
    number_calls= []
    def timer() -> None:
        for _ in range(5):
            start = time.perf_counter()
            f = func()
            finish = time.perf_counter()
            number_calls.append(finish - start)
        avg_time = sum(number_calls)/5
        print(f"Время: {avg_time:.6f} сек.")
        print("Результат:", f)

    return timer



@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

compute()

#f = compute()
#print("Результат:", f)

# Среднее время выполнения для 5 вызовов: 0.47 секунд
# 49999995000000