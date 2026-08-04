""" 02 Города выбранной страны

Добавьте к предыдущей программе возможность выбора страны.
Пользователь должен ввести название страны.
Далее выведите все города этой страны и их численность населения.

Пример вывода 1:
Введите страну: Germany
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560

Пример вывода 2:
Введите страну: Unknown
❌ Страна 'Unknown' не найдена
...

"""

import mysql.connector
from local_settings import dbconfig
from mysql.connector import Error


class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""


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

    def fetch_cities_by_country(self, country_name):
        """Получить все города выбранной страны с их населением"""
        self._ensure_cursor()

        try:
            self.cursor.execute("""SELECT city.Name, city.District, city.Population
                                   FROM world.city
                                            JOIN world.country ON city.CountryCode = country.Code
                                   WHERE country.Name = %s
                                   ORDER BY city.Population DESC"""
                                , (country_name,), )

            rows = self.cursor.fetchall()

            return [
                row if isinstance(row, dict) else row[0]
                for row in rows
            ]

        except Error as e:
            raise DatabaseError("Не удалось получить список городов") from e


if __name__ == "__main__":
    try:
        with WorldDB(dbconfig, True) as db:
            # Список всех стран
            countries = db.fetch_countries()
            print("Список стран:")
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")

            # Ввод страны пользователем
            country_input = input("\nВведите страну: ").strip()

            # Получаем города выбранной страны
            cities = db.fetch_cities_by_country(country_input)
            if not cities:
                print(f"Для страны '{country_input}' нет данных о городах.")
            else:
                for city in cities:
                    # Формируем строку с названием города и населением
                    city_name = city['Name']
                    district = city['District']
                    population = city['Population']
                    # Если нужно — можно добавить район/альтернативное имя
                    print(f"{city_name} — {district} - {population}")

    except DatabaseError as e:
        print(f"❌ {e}")
