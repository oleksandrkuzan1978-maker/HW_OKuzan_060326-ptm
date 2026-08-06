""" 02. Увеличение цен

Продолжите предыдущую задачу. Теперь программа должна:
- увеличить цену всех товаров на 20%
- вывести количество обновлённых записей
- затем вывести список всех товаров с новыми ценами

Пример вывода:
Prices updated for 3 products.

Updated products:
- Pen — $1.80
- Notebook — $4.79
- Backpack — $30.00"""

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
    collection.insert_many(products)
    result = collection.update_many({},[
        {
            "$set": {
                "price": {
                    "$multiply": ["$price", 1.2]
                }
            }
        }
    ])
    print(f"Prices updated for {result.modified_count} products.\n")

    print("Updated products:")
    for doc in collection.find({}, {"_id": 0, "name": 1, "price": 1}):
        print(f"- {doc['name']} - ${doc['price']}")


# Prices updated for 3 products.
#
# Updated products:
# - Laptop — $1440.00
# - Mouse — $30.00
# - Keyboard — $84.00