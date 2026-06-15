""" 01 Деление без ошибок

Напишите функцию, которая
- выполняет деление двух чисел, введенных пользователем,
- и обрабатывает возможные ошибки.

ВАЖНО: Используйте несколько обработок различных ошибок

Примеры вывода:

Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число.

Введите делимое: 5
Введите делитель: 0
Ошибка: Деление на ноль невозможно.

Введите делимое: 5
Введите делитель: 2
Результат: 2.5

"""


# Вариант №1
def safe_division(dividend, divisor):
    if not isinstance(dividend, (int, float)):
        raise TypeError("Ошибка: Делимое должно быть числом")
    if not isinstance(divisor, (int, float)):
        raise TypeError("Ошибка: Делитель должен быть числом")
    if divisor == 0:
        raise ZeroDivisionError("Ошибка: Деление на ноль запрещено!")
    return dividend / divisor


# Пример вызова функции
for dividend, divisor in [('a', 5), (5, 0), (5, 2), ('5.5', '1.2')]:
    try:
        print(f"Результат деления: {safe_division(dividend, divisor)}")
    except (TypeError, ZeroDivisionError) as e:
        print(e)


# Вариант №2
def safe_division():
    try:
        dividend = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))
        return dividend / divisor
    except ValueError:
        print("Ошибка: нужно ввести число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль запрещено")
    except Exception:
        print("Ошибка при выполнении функции")
    return None


res = safe_division()
if res is not None:
    print(f"Результат деления: {res}")
