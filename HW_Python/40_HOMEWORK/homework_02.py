""" 02. Класс для работы с деньгами

Создайте класс Money, в котором можно:
- складывать и вычитать объекты через операторы + и -
- выводить объект как строку в виде "$<amount>"
- при сложении и вычитании возвращается новый объект
- если вычитание приводит к отрицательному значению — вернуть 0

Пример использования:
money1 = Money(100)
money2 = Money(50)

print(money1 + money2)
print(money1 - money2)
print(money2 - money1)

Пример вывода:
$150
$50
$0
"""

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented

        return Money(self.amount + other.amount)

    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(max(self.amount - other.amount, 0))

    def __str__(self):
        return f"${self.amount}"


# Пример использования
money1 = Money(100)
money2 = Money(50)

print(money1 + money2)  # $150
print(money1 - money2)  # $50
print(money2 - money1)  # $0

# $150
# $50
# $0

