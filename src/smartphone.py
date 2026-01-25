from src.product import Product


class Smartphone(Product):
    """Подкласс класса Product для описания доп. свойств смартфонов"""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.color = color
