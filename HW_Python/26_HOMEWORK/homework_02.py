""" 02 Поиск и удаление файлов с указанным расширением

Напишите программу, которая
- Принимает путь к директории и расширение файлов через аргумент командной строки.
- Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
- Спрашивает у пользователя, хочет ли он удалить найденные файлы.
- Если пользователь подтверждает, удаляет их.

Пример запуска
python script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os
import sys


s = "python homework_02.py D:\\a_WEITERBILDUNG\\PYTHON\WORKS\\26__file_system\\HOMEWORK .log"

def find_files_with_extension(directory:str, extension:str) -> NoneType:
    """Рекурсивно ищет файлы с заданным расширением."""
    if os.path.exists(directory):
        files_for_delete = [] # Список для файлов, подлежащих удалению (c указанием пути к каждому файлу)

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension): # есть ли файлы с нужным расширением
                    files_for_delete.append(os.path.join(root, file))

        if files_for_delete:
            print(f"Найдены файлы с расширением {extension}:")
            for f in files_for_delete:
                print("- ", f)
                # Организация процесса удаления файлов
            while True:
                request = input("Вы хотите удалить эти файлы? (y/n): ")
                if request == "y" or request == "n":
                    if request == "y":
                        for f in files_for_delete:
                            os.remove(f)
                        print("Файлы удалены")
                    break
                print("Ошибка! Неверный символ. Попробуйте еще раз 'y' или 'n'")
        else:
            print(f"Файлы c расширением {extension} в директории {os.path.basename(directory)} и ее поддиректориях не найдены")
    else:
        print("Вы ввели неверный путь. Такого пути не существует.")

find_files_with_extension(sys.argv[1], sys.argv[2])

#Предварительно создаём ненужные файлы для удаления
# files = [
#     'error.log',
#     'system.log',
#     'logs\\old.log',
#     'logs\\debug.log',
# ]
#
# for file in files:
#     with open(file, 'w') as f:
#         f.write("")




