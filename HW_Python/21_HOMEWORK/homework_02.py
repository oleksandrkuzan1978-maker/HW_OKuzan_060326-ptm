"""Группировка студентов по классам

Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.
Данные:
students = [("class1", "Alice"),
            ("class2", "Bob"),
            ("class1", "Charlie"),
            ("class3", "Daisy")]
Пример вывода:
{
    'class1': ['Alice', 'Charlie'],
    'class2': ['Bob'],
    'class3': ['Daisy']
}"""
from collections import defaultdict
from pprint import pprint

def get_students_groups(students):
    sample = defaultdict(list)
    for class_num, student in students:
        sample[class_num].append(student)
    return dict(sample)


students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
res = get_students_groups(students)
# Вариант вывода №1
pprint(res, width=35)
# Вариант вывода №2
print("{")
for class_num, names in res.items():
    print(f"    '{class_num}': {names},")
print("}")
