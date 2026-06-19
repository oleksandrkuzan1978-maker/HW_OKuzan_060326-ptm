"""01 Список файлов и папок

Напишите программу, которая
- принимает путь к директории через аргумент командной строки
- и выводит:
    - Отдельно список папок
    - Отдельно список файлов

Пример запуска:
python script.py /home/user/documents

Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx
"""

import sys
import os

path = sys.argv[1]  # берем из командной строки путь
directories, files = [], []

for item in os.listdir(path): # создаем список файлов и папок в директории и перебираем их
    full_path = os.path.join(path, item) # правильно соединяем части пути
    if os.path.isfile(full_path): # проверяем, является ли объект по пути full_path файлом
        files.append(item)
    elif os.path.isdir(full_path): # проверяем, является ли объект по пути full_path директорией
        directories.append(item)

print("Папки: ")
for dir in directories:
    print("-", dir)

print("Файлы: ")
for file in files:
    print("-", file)

