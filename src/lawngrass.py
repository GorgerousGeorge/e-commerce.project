from src.product import Product


class LawnGrass(Product):
    """Класс для описания товаров подкатегории трава газонная. В дополнение к стандартному набору аттрибутов указываем
    страна-производитель, срок прорастания и цвет"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
