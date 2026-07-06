""" 02 Генератор уникальных элементов

Создайте генератор, который
- принимает список элементов и выдаёт только уникальные значения,
сохраняя порядок их появления в исходном списке

Входные данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

Пример вывода:
3
1
2
4
5
6
7
8

"""

from typing import Generator, Any

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]


def generator_unique(items: list[Any]) -> Generator[Any, None, None]:
    set_items = set()
    for item in items:
        if item not in set_items:
            set_items.add(item)
            yield item

for x in generator_unique(data):
    print(x)

# 3
# 1
# 2
# 4
# 5
# 6
# 7
# 8