""" 01 Фильтрация по ключевому слову

Напишите программу, которая
- ищет в файле все строки, содержащие указанное пользователем слово,
- и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в <keyword>_<original_filename>.

"""

def find_keyword(filename: str, keyword: str) -> None:

    matches = []
    file_out_name = f"{keyword}_{filename}"

    with open(filename, "r", encoding="utf-8") as file_in:

        for line in file_in:
            if keyword in line:
                matches.append(line)

    if not matches:
        print(f"Слово '{keyword}' в файле {filename} не найдено")
    else:
        with open(file_out_name, "a", encoding="utf-8") as file_out:
            file_out.writelines(matches)
        print(f"Строки, содержащие '{keyword}', сохранены в {file_out_name}")


try:
    #find_keyword('s', 'error')
    #File not found: [Errno 2] No such file or directory: 's'

    find_keyword('system_log.txt', 'eror')
    # Строки, содержащие 'error', сохранены в error_system_log.txt.
except FileNotFoundError as e:
    print("File not found:", e)



