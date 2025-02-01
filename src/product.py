class Product:
    """Класс для описания товаров. Также указаны цена и имеющееся в наличии количество"""
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса Product. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, name, description, price, quantity, list_of_products: list):
        """Метод для создания новых объектов класса Product. На вход необходимо подать словарь с параметрами товаров"""
        for product in list_of_products:
            if name == product:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return product
        return cls(name, description, price, quantity)
