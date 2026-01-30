# from src.product import Product
#
#
# class Category:
#     """Класс для описания категорий продуктов"""
#
#     name: str
#     description: str
#     products: list
#     category_count = 0
#     product_count = 0
#
#     def __init__(self, name, description, products=None):
#         self.name = name
#         self.description = description
#         self.__products = products if products else []
#         Category.category_count += 1
#         Category.product_count += len(products) if products else 0
#
#     def __str__(self) -> str:
#
#         product_quantity = sum(item.quantity for item in self.__products)
#         return f"{self.name}, количество продуктов: {int(product_quantity)} шт."
#
#     def add_product(self, product: Product):
#         if isinstance(product, Product):
#             self.__products.append(product)
#             Category.product_count += 1
#         else:
#             raise TypeError
#
#     @property
#     def products(self):
#         products_str = ""
#         for product in self.__products:
#             products_str += f"{str(product)}\n"
#         return products_str
#
#     @property
#     def products_in_list(self):
#         return self.__products
