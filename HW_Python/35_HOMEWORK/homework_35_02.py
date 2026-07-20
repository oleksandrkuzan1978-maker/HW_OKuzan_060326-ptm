""" 02. Проверка данных пользователя

Доработайте класс User.
- Добавьте валидации полей при создании.
- Имя должно быть непустой строкой.
- Пароль должен быть строкой длиной не менее 5 символов.
- Если данные некорректны — выбрасывайте ValueError.
- Добавьте строковое представление объекта.
- Проверьте работу класса с разными значениями.
"""

class User:
    total_users = 0

    def __init__(self, username, password):
        self.username = username
        self.password = password

        if not isinstance(self.username, str) or self.username == "":
            raise ValueError("Username must be a non-empty string.")
        if not isinstance(self.password, str) or len(self.password) < 5:
            raise ValueError("Password must be a string with at least 5 characters.")
        self.__class__.total_users += 1

    def __str__(self):
        return f"User(username='{self.username}')"

    @classmethod
    def get_total(cls):
        return cls.total_users


try:
    user1 = User("alice", "pass123")
    print(user1)  # User(username='alice')
except ValueError as e:
    print("Error:", e)

try:
    user2 = User("", "12345")  # Некорректное имя
except ValueError as e:
    print("Error:", e)

try:
    user3 = User("bob", "123")  # Слишком короткий пароль
except ValueError as e:
    print("Error:", e)

print(f"Total users: {User.get_total()}")
# Должно быть 1, только валидные пользователи считаются


# User(username='alice')
# Error: Username must be a non-empty string.
# Error: Password must be a string with at least 5 characters.
# Total users: 1