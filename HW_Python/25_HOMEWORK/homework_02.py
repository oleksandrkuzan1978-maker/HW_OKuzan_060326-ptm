""" 02 Логирование ошибок

Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log
в соответствии с форматом ниже.

ВАЖНО: используйте вывод ошибок
    - и в файл,
    - и на экран.

Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

"""

import logging
# Создаём два хендлера
file_handler = logging.FileHandler("errors.log", mode="w", encoding="utf-8") # Для вывода в лог-файл
console_handler = logging.StreamHandler()       # Для вывода в консоль

# Настраиваем формат вывода logging-сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - Ошибка: %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Конфигурация root logger через basicConfig
logging.basicConfig(
    level=logging.ERROR,
    handlers=[file_handler, console_handler],
    force=True)

logger = logging.getLogger(__name__) # создал дочерний логгер для этого модуля (как тренировка, на будущее)

def safe_division():
    try:
        dividend = float(input("Введите делимое: "))
        divisor = float(input("Введите делитель: "))
        return dividend / divisor
    except ValueError:
        loggеr.error("Нужно ввести число")
    except ZeroDivisionError:
        logger.error("Деление на ноль запрещено")
    except Exception as e:
        logger.error(f"{e}")
    return None


res = safe_division()
if res is not None:
    print(f"Результат деления: {res}")

# Вариант №1
# def safe_division(dividend, divisor):
#     if not isinstance(dividend, (int, float)):
#         raise TypeError("Ошибка: Делимое должно быть числом")
#     if not isinstance(divisor, (int, float)):
#         raise TypeError("Ошибка: Делитель должен быть числом")
#     if divisor == 0:
#         raise ZeroDivisionError("Ошибка: Деление на ноль запрещено!")
#     return dividend / divisor
#
#
# # Пример вызова функции
# for dividend, divisor in [('a', 5), (5, 0), (5, 2), ('5.5', '1.2')]:
#     try:
#         print(f"Результат деления: {safe_division(dividend, divisor)}")
#     except (TypeError, ZeroDivisionError) as e:
#         logger.error(e)


