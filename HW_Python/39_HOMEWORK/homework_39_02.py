""" 02 Проверка размеров фигур

Доработайте фигуры:
Добавьте проверку в инстанцирование Circle и Rectangle,
чтобы значения были строго положительными.
Если передано отрицательное или нулевое значение,
выбрасывайте пользовательское исключение InvalidSizeError.
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


class InvalidSizeError(ValueError):
    def __init__(self, name: str, value: float | int):
        super().__init__(f"Значение {name}={value} должно быть положительным")


class Circle(Shape):

    def __init__(self, radius):
        if radius <= 0:
            raise InvalidSizeError("radius", radius)

        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, width, height):
        if height <= 0:
            raise InvalidSizeError("height", height)
        if width <= 0:
            raise InvalidSizeError("width", width)

        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width


if __name__ == "__main__":
    try:
        c = Circle(-5)
    except InvalidSizeError as e:
        print("Ошибка:", e)

    try:
        r = Rectangle(3, 0)
    except InvalidSizeError as e:
        print("Ошибка:", e)

# Ошибка: Значение radius=-5 должно быть положительным!
# Ошибка: Значение height=0 должно быть положительным!
