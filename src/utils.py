# import json
# import os
#
# from src.category import Category
# from src.product import Product
#
#
# def read_json_file(filepath: str) -> dict:
#     """Читает json-файл"""
#
#     full_filepath = os.path.abspath(filepath)
#     with open(full_filepath, "r", encoding="UTF-8") as file:
#         data = json.load(file)
#     return data
#
#
# def create_objects_from_json(data) -> list:
#     """Преобразует данные формата json в список категорий с товарами"""
#
#     categories_list = []
#     for category in data:
#         products = []
#         for product in category["products"]:
#             products.append(Product(**product))
#         category["products"] = products
#         categories_list.append(Category(**category))
#
#     return categories_list
