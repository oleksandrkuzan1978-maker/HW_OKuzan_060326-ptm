""" 02 Добавление заметок

Продолжите предыдущую программу:
- создайте таблицу notes с полями: id, title, content
- вставьте одну заметку в таблицу
- выполните commit() после вставки
- выведите все заметки используя в формате dict (а не tuple!)

Пример вывода:

All notes:
{'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}

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
            if self.connection is not None:
                if exc_type is None:
                    self.connection.commit()
                else:
                    self.connection.rollback()

        except Error as error:
            raise DatabaseError(
                "Ошибка завершения транзакции"
            ) from error

        finally:
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

    ALLOWED_TABLES = {
        "notes",
    }

    @staticmethod
    def _validate(name, allowed_names, object_type):
        """Возвращает имя, если оно входит в белый список."""
        if name not in allowed_names:
            raise ValueError(
                f"Недопустимое имя {object_type}: {name!r}"
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

    @classmethod
    def table(cls, name):
        """Проверяет имя таблицы."""
        return cls._validate(
            name,
            cls.ALLOWED_TABLES,
            "таблицы",
        )

class SchemaManager:
    """Управляет структурой базы данных заметок."""

    def __init__(self, cursor, db_name, table_name):
        """Сохраняет курсор и проверенные SQL-идентификаторы."""
        self.cursor = cursor
        self.db_name = IdentifierValidator.database(db_name)
        self.table_name = IdentifierValidator.table(table_name)

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
                f"базу {self.db_name!r}"
            ) from error

    def create_table(self):
        """Создаёт таблицу заметок при её отсутствии."""
        try:
            self.cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS
                `{self.table_name}` (
                    id INT UNSIGNED AUTO_INCREMENT
                        PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    content TEXT NOT NULL
                )
                """
            )

        except Error as error:
            raise DatabaseError(
                f"Не удалось создать таблицу "
                f"{self.table_name}"
            ) from error

    def drop_table(self):
        """Удаляет таблицу."""
        try:
            self.cursor.execute(f"""DROP table if exists {self.table_name}""")

        except Error as error:
            raise DatabaseError(
                f"Не удалось удалить таблицу "
                f"{self.table_name}"
            ) from error

class NoteRepository:
    """Предоставляет операции доступа к заметкам."""

    def __init__(self, cursor, table_name):
        """Сохраняет курсор и проверенное имя таблицы."""
        self.cursor = cursor
        self.table_name = IdentifierValidator.table(table_name)

    def add_note(self, title, content):
        """Добавляет заметку с указанными заголовком и текстом."""
        try:
            self.cursor.execute(
                f"""
                INSERT INTO `{self.table_name}`
                    (title, content)
                VALUES (%s, %s)
                """,
                (title, content),
            )

        except Error as error:
            raise DatabaseError(
                "Не удалось добавить заметку"
            ) from error

    def get_all(self):
        """Возвращает все заметки в порядке их идентификаторов."""
        try:
            self.cursor.execute(
                f"""
                SELECT id, title, content
                FROM `{self.table_name}`
                ORDER BY id
                """
            )
            return self.cursor.fetchall()

        except Error as error:
            raise DatabaseError(
                "Не удалось получить заметки"
            ) from error


if __name__ == "__main__":

    database_name = "notes_app_060326_ptm_oleksandr_kuzan"
    table_name = "notes"
    insert_data = ("First Note",
                   "This is the content of my first note.")

    server_config = dbconfig_write.copy()
    server_config.pop("database", None)

    try:
        with MySQLConnection(
            server_config,
            is_dict=True,
        ) as session:
            schema = SchemaManager(
                session.cursor,
                database_name,
                table_name,
            )

            schema.create_database()
            print(
                f"Database {database_name} "
                "created or already exists."
            )

            schema.create_table()
            print(f"Table '{table_name}' is created or already exists")

            notes = NoteRepository(
                session.cursor,
                table_name,
            )

            notes.add_note(*insert_data)


            print("All notes:")
            for note in notes.get_all():
                print(note)


    except DatabaseError as error:
        print(f"Ошибка базы данных: {error}")

    except ValueError as error:
        print(f"Некорректное имя: {error}")




