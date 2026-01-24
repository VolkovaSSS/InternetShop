class Product:
    """Класс для описания продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return (
            f"{self.name}, {int(self.__price)} руб. Остаток: {int(self.quantity)} шт."
        )

    def __add__(self, other) -> float:
        return round(self.quantity * self.__price + other.quantity * other.__price, 2)

    @classmethod
    def new_product(cls, product_params: dict):
        return cls(**product_params)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
