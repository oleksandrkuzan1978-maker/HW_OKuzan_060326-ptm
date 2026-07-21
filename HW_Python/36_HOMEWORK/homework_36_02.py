""" 02 Класс Student

На основе класса Person создайте класс Student.
- Студент должен иметь имя и номер курса.
- Метод introduce() должен
    - сначала выводить базовое приветствие,
    - а затем строку: I'm on course <номер_курса>.

Пример вывода:
Hello, my name is Alice.
I'm on course 2.
"""


class Person:

    def __init__(self, name: str):
        self.name = name

    def introduce(self) -> None:
        print(f"Hello, my name is {self.name}.")


class Student(Person):

    def __init__(self, name: str, num_class: int):
        super().__init__(name)
        self.num_class = num_class

    def introduce(self) -> None:
        super().introduce()
        print(f"I'm on course {self.num_class}.")


st1 = Student("Alice", 2)
st1.introduce()

# Hello, my name is Alice.
# I'm on course 2.

