from src.product import Product


class Smartphone(Product):
    """Класс для описания товаров подкатегории смартфон. В дополнение к стандартному набору аттрибутов указываем
    производительность, модель, объем памяти и цвет"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
