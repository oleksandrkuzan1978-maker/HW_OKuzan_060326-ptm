""" 01 Список всех стран

Используя базу данных world, вывести названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe

Попробуйте решить задачи используя стиль Data Access Object (DAO).
"""

import mysql.connector
from local_settings import dbconfig
from mysql.connector import Error

class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""
    pass


class MySQLConnection:
    def __init__(self, db_config, is_dict=False):
        self.dbconfig = db_config
        self.is_dict = is_dict
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(**self.dbconfig)
            self.cursor = self.connection.cursor(dictionary=self.is_dict)
            return self

        except Error as e:
            # Если соединение успело открыться, а курсор создать не удалось
            if self.connection is not None:
                self.connection.close()
            raise DatabaseError(
                "Не удалось подключиться к базе данных"
            ) from e

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.cursor is not None:
                self.cursor.close()
        finally:
            if self.connection is not None:
                self.connection.close()

        return False


class WorldDB(MySQLConnection):

    def _ensure_cursor(self):
        """Метод проверки на случай, если методы будут вызваны вне контекстного менеджера"""
        if self.cursor is None:
            raise DatabaseError("Метод должен вызываться внутри блока with")


    def fetch_countries(self):
        """Получить список всех стран"""
        self._ensure_cursor()

        try:
            self.cursor.execute("SELECT name FROM world.country")
            rows = self.cursor.fetchall()

            return [
                row["name"] if isinstance(row, dict) else row[0]
                for row in rows
            ]

        except Error as e:
            raise DatabaseError("Не удалось получить список стран") from e


if __name__ == "__main__":
    try:
        with WorldDB(dbconfig, True) as db:
            countries = db.fetch_countries()
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")
    except DatabaseError as e:
        print(f"❌ {e}")
