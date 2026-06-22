""" 02 Поиск и удаление дубликатов

Напишите программу, которая
- удаляет дублирующиеся строки из файла
- и сохраняет результат в новый файл.

Имя нового файла формируется как unique_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

"""
# ВАРИАНТ №1
from collections import OrderedDict

def remove_duplicates(filename: str) -> None:

    with open(filename, "r", encoding="utf-8") as origin_file:
        uniq_lines = list(OrderedDict.fromkeys(origin_file)) # В качестве ключей словаря - строки файла (файл - итератор)
                                                             # Значения словаря по умолчанию = None.

    with open(f"unique_{filename}", "w", encoding="utf-8") as uniq_file_out:
        uniq_file_out.writelines(uniq_lines)
    print(f"Дубликаты удалены. Уникальные строки сохранены в unique_{filename}.")


# ВАРИАНТ №2
# def remove_duplicates(filename: str) -> None:
#
#     uniq_lines = []
#
#     with open(filename, "r", encoding="utf-8") as origin_file:
#         for line in origin_file:
#             if line not in uniq_lines:
#                 uniq_lines.append(line)
#
#     with open(f"unique_{filename}", "w", encoding="utf-8") as file:
#         file.writelines(uniq_lines)
#     print(f"Дубликаты удалены. Уникальные строки сохранены в unique_{filename}.")


# ВАРИАНТ №3 (Для больших объемов данных)
# def remove_duplicates(filename: str) -> None:
#
#     set_uniq_lines = set()
#     uniq_lines = []
#
#     with open(filename, "r", encoding="utf-8") as origin_file:
#         for line in origin_file:
#             if line not in set_uniq_lines:
#                 set_uniq_lines.add(line) # Кешируемый быстро проверяется при проверке
#                 uniq_lines.append(line) # Списком гарантируем сохранение порядка строк
#
#     with open(f"unique_{filename}", "w", encoding="utf-8") as file:
#         file.writelines(uniq_lines)
#     print(f"Дубликаты удалены. Уникальные строки сохранены в unique_{filename}.")



try:
    remove_duplicates("movies_to_watch.txt")
    # Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

    #remove_duplicates("M")
    # File not found: [Errno 2] No such file or directory: 'M'
except FileNotFoundError as e:
    print("File not found:", e)




