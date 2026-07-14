""" 02 Среднее время выполнения с количеством вызовов

Доработайте декоратор measure_time, чтобы он
- принимал параметр repeats — количество вызовов функции.

Декоратор должен
- выполнять функцию указанное число раз
- и выводить среднее время выполнения.

Пример применения:
@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

Пример вывода:
Среднее время выполнения для 10 вызовов: 0.21 секунд
Результат: 49999995000000

"""
import time
from typing import Callable

def measure_time(times: int=5) -> Callable:
    def func_transmitter(func: Callable):
        number_calls= []
        def timer() -> None:
            for _ in range(times):
                start = time.perf_counter()
                f = func()
                finish = time.perf_counter()
                number_calls.append(finish - start)
            avg_time = sum(number_calls)/times
            print(f"Среднее время выполнения ф-ции за {times} вызовов: {avg_time:.6f} сек.")
            print("Результат:", f)
        return timer
    return func_transmitter


@measure_time(10)
def compute() -> int:
    total = 0
    for i in range(10_000_000):
        total += i
    return total


compute()


# Среднее время выполнения для 10 вызовов: 0.49 секунд
# 49999995000000