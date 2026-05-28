""" 01 Простое число

Напишите функцию is_prime(), которая
- проверяет, является ли число n простым (делится только на 1 и само себя)
- и возвращает булев результат.


Пример проверки функции is_prime():

chack_func_is_prime(17)  # Число 17 является простым
chack_func_is_prime(18)  # Число 18 НЕ является простым
"""


# Вариант №1
def is_prime(n):
    # Ф-ция проверяет, является ли число n простым
    if n <= 1:  # Число НЕ является простым
        return False
    end_range = int(n ** 0.5) + 1
    for i in range(2, end_range):
        if n % i == 0:  # Число НЕ является простым
            return False
    return True  # Является простым


def chack_func_is_prime(n):
    text = "является" if is_prime(n) else "НЕ является"
    print(f"Число {n} {text} простым")


chack_func_is_prime(17)  # Число 17 является простым
chack_func_is_prime(18)  # Число 18 НЕ является простым


# Вариант №2
def is_prime(n):
    # Ф-ция проверяет, является ли число n простым
    if n <= 1:  # Число НЕ является простым
        return False
    end_range = int(n ** 0.5) + 1
    for i in range(2, end_range):
        if n % i == 0:  # Число НЕ является простым
            return False


def chack_func_is_prime(n):
    text = "является" if is_prime(n) == None else "НЕ является"
    print(f"Число {n} {text} простым")


chack_func_is_prime(17)  # Число 17 является простым
chack_func_is_prime(18)  # Число 18 НЕ является простым
