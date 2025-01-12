import json
import os

from src.category import Category
from src.product import Product


def json_reader(path: str):
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def object_creator(data):
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories

def object_creator_from_json(path:str):
    return object_creator(json_reader(path))
