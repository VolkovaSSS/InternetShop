# import pytest
#
# from src.category import Category
# from src.lawngrass import LawnGrass
# from src.product import Product
# from src.product_iterator import ProductIterator
# from src.smartphone import Smartphone
#
#
# @pytest.fixture
# def first_category():
#     return Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации и получения дополнительных функций",
#         [
#             Product(
#                 "Samsung Galaxy S23 Ultra",
#                 "256GB, Серый цвет, 200MP камера",
#                 180000.0,
#                 5,
#             ),
#             Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
#         ],
#     )
#
#
# @pytest.fixture
# def second_category():
#     return Category(
#         "Телевизоры",
#         "Современный телевизор, который позволяет наслаждаться просмотром",
#         [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
#     )
#
#
# @pytest.fixture
# def product_test2():
#     return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#
#
# @pytest.fixture
# def product_test3():
#     return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#
# @pytest.fixture
# def product_iterator_for_test(first_category):
#     return ProductIterator(first_category)
#
#
# @pytest.fixture
# def smartphone_test1():
#     return Smartphone(
#         "Samsung Galaxy S23 Ultra",
#         "256GB, Серый цвет, 200MP камера",
#         180000.0,
#         5,
#         95.5,
#         "S23 Ultra",
#         256,
#         "Серый",
#     )
#
#
# @pytest.fixture
# def smartphone_test2():
#     return Smartphone(
#         "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
#     )
#
#
# @pytest.fixture
# def grass_test1():
#     return LawnGrass(
#         "Газонная трава",
#         "Элитная трава для газона",
#         500.0,
#         20,
#         "Россия",
#         "7 дней",
#         "Зеленый",
#     )
#
#
# @pytest.fixture
# def grass_test2():
#     return LawnGrass(
#         "Газонная трава 2",
#         "Выносливая трава",
#         450.0,
#         15,
#         "США",
#         "5 дней",
#         "Темно-зеленый",
#     )
