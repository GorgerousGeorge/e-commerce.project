class Category:
    """Класс для категорий товаров"""
    name = str
    description = str
    products = list

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products
