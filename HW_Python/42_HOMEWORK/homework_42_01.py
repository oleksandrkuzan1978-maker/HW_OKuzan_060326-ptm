""" 01 Создание базы

Напишите программу, которая:
- создаёт базу данных notes_app_<your_group>_<your_full_name>
- выбирает эту базу через USE notes_app
- выводит сообщение о результате

Пример вывода:
Database 'notes_app' created or already exists.
"""


import mysql.connector
from mysql.connector import Error

from local_settings import dbconfig_write

class DatabaseError(Exception):
    """Общая ошибка слоя доступа к данным."""


class MySQLConnection:
    """Управляет подключением, транзакцией и курсором MySQL."""

    def __init__(self, db_config, is_dict=False):
        """Сохраняет настройки будущего подключения к MySQL."""
        self.db_config = db_config
        self.is_dict = is_dict
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """Открывает соединение и возвращает текущую сессию."""
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            self.cursor = self.connection.cursor(dictionary=self.is_dict)
            return self

        except Error as error:
            if self.connection is not None:
                self.connection.close()

            raise DatabaseError(
                "Не удалось подключиться к серверу MySQL"
            ) from error

    def __exit__(self, exc_type, exc_value, traceback):
        """Завершает транзакцию и закрывает ресурсы MySQL."""
        try:
            if self.cursor is not None:
                self.cursor.close()
        finally:
            if self.connection is not None:
                self.connection.close()

        return False

class IdentifierValidator:
    """Проверяет допустимость SQL-идентификаторов."""
    ALLOWED_DATABASES = {
        "notes_app_060326_ptm_oleksandr_kuzan",
    }

    @staticmethod
    def _validate(name, allowed_names, object_type):
        """Возвращает имя, если оно входит в белый список."""
        if name not in allowed_names:
            raise ValueError(
                f"Недопустимое имя {object_type}: {name}"
            )

        return name

    @classmethod
    def database(cls, name):
        """Проверяет имя базы данных."""
        return cls._validate(
            name,
            cls.ALLOWED_DATABASES,
            "базы данных",
        )


class SchemaManager:
    """Управляет структурой базы данных заметок."""

    def __init__(self, cursor, db_name):
        """Сохраняет курсор и проверенные SQL-идентификаторы."""
        self.cursor = cursor
        self.db_name = IdentifierValidator.database(db_name)

    def create_database(self):
        """Создаёт базу данных при необходимости и выбирает её."""
        try:
            self.cursor.execute(
                f"""
                CREATE DATABASE IF NOT EXISTS
                `{self.db_name}`
                """
            )
            self.cursor.execute(
                f"USE `{self.db_name}`"
            )

        except Error as error:
            raise DatabaseError(
                f"Не удалось создать или выбрать "
                f"базу {self.db_name}"
            ) from error



if __name__ == "__main__":

    database_name = "notes_app_060326_ptm_oleksandr_kuzan"
    table_name = "notes"

    server_config = dbconfig_write.copy()
    server_config.pop("database", None)

    try:
        with MySQLConnection(server_config) as session:

            schema = SchemaManager(
                session.cursor,
                database_name,
            )

            schema.create_database()

            print(
                f"Database {database_name} "
                "created or already exists."
            )


    except DatabaseError as error:
        print(f"Ошибка базы данных: {error}")

    except ValueError as error:
        print(f"Некорректное имя: {error}")