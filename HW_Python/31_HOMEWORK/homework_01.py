"""Извлечение дат
Реализуйте программу, которая должна:
Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

Данные:
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."


Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022

"""
text = "The events N 123456 happened on 15/03/2025, 01.12.2024 and 09-09-2023. Deadline: 28/02/2022."

import re

#result = re.finditer(r"\d{2}/\d{2}/\d{4}|\d{2}.\d{2}.\d{4}|\d{2}-\d{2}-\d{4}", text)
result = re.finditer(r"\d{2}(/|.|-)\d{2}\1\d{4}", text)
for item in result:
    print(item.group(0))




# 15/03/2025
# 01.12.2024
# 09-09-2023
# 28/02/2022