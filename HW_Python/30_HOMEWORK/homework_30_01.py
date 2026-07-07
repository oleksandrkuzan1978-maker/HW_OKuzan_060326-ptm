"""01 Анализ курсов студентов

Реализуйте программу, которая должна:
1. Прочитать файл student_courses.json, содержащий:
    - Имя
    - дату рождения (birth_date) в формате дд.мм.гггг
    - дату поступления (enrollment_date) в том же формате
    - список курсов.

2. Вычислить:
    - общее количество студентов.
    - средний возраст на момент поступления.
    - количество студентов на каждом курсе.

3. Сохранить отчёт в JSON-файл student_courses_report.json.
"""

import json
from collections import Counter
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as rld


INPUT_FILE = "student_courses.json"
OUTPUT_FILE = "student_courses_report.json"

# Чтение JSON-файла и преобразование его содержимого в Python-объект
def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

# Сохранение отчета в JSON-файл
def write_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def get_info():
    """
    "name": "Diana Williams",
    "birth_date": "12.06.1983",
    "enrollment_date": "29.04.2023",
    "courses": [
      "Physics",
      "Chemistry"
    ]
    """
    data = read_json(INPUT_FILE)

    course_counter = Counter()

    sum_ages = 0
    ns = len(data) # Общее кол-во студентов

    for student in data:
        date_enrollment = dt.strptime(student["enrollment_date"], "%d.%m.%Y") # строку в дату
        date_birth = dt.strptime(student["birth_date"], "%d.%m.%Y") # строку в дату
        age = rld(date_enrollment, date_birth).years # Возраст каждого студента на момент поступления
        sum_ages += age
        course_counter.update(student["courses"]) # Объект Counter создает словарь в котором ключи - наименования курсов
                                                  # Метод update увеличивает значение ключа на 1

    report = {"total_students": ns,
              "average_enrollment_age": round(sum_ages/ns, 1),
              "students_per_course": dict(course_counter)}

    write_json(report, OUTPUT_FILE)

    print("Отчет успешно сохранен в student_courses_report.json")
    print(json.dumps(report, indent=8, ensure_ascii=False))


get_info()
