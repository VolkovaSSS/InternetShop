# from src.product import Product
#
#
# class LawnGrass(Product):
#     """Подкласс класса Product для описания доп. свойств продуктов Трава газонная"""
#
#     country: str
#     germination_period: str
#     color: str
#
#     def __init__(
#         self, name, description, price, quantity, country, germination_period, color
#     ):
#
#         super().__init__(name, description, price, quantity)
#         self.country = country
#         self.germination_period = germination_period
#         self.color = color
#
#     def __add__(self, other) -> float:
#
#         if type(other) is LawnGrass:
#             return round(self.quantity * self.price + other.quantity * other.price, 2)
#         else:
#             raise TypeError
