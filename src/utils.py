import json
from typing import Any

from src.product_category import Category, Product


def read_json(file_json: str) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей."""

    with open(file_json, "r", encoding="utf-8") as f:
        try:
            prod = json.load(f)
            return prod

        except:
            return []


# print(
#     json.dumps(
#         read_json(r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json"),
#         indent=4,
#     )
# )


def new_objects(prod: dict) -> Any:
    """Функция, которая принимает на список словарей
    и создает объекты классов."""
    categories = []
    for category in prod:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":
    info = read_json(r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json")
    new = new_objects(info)
    print(new[0].name)
    print(new[0].description)
    print(new[0].products[0].name)
    print(new[0].products[1].name)
    print(new[0].products[2].name)
    print(new[1].name)
    print(new[1].description)
    print(new[1].products[0].name)
