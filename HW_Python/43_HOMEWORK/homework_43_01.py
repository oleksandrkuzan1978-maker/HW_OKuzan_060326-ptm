""" 01 Добавление товаров

Создайте программу, которая подключается к MongoDB и:
- выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
- очищает коллекцию перед началом
- добавляет 3 товара с полями: name, price, stock
- выводит сообщение о количестве добавленных товаров
Пример вывода:
3 products inserted.
"""


from pymongo import MongoClient
from local_settings import MONGODB_URL_WRITE

products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 50},
    {"name": "Keyboard", "price": 70, "stock": 20}
]
DB_NAME = "ich_edit"
COLLECTION_NAME = "products_060326_ptm_Oleksandr_Kuzan"

with MongoClient(MONGODB_URL_WRITE) as client:
    collection = client[DB_NAME][COLLECTION_NAME]
    collection.delete_many({})
    result = collection.insert_many(products)
print(len(result.inserted_ids),"products inserted")


# 3 products inserted.
