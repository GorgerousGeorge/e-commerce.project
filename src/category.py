from src.product import Product


class Category:
    """Класс для категорий товаров"""
    name = str
    description = str
    products = list
    count_category = 0
    count_of_goods = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = list(products)
        Category.count_category += 1
        Category.count_of_goods += len(products)

    def add_product(self, new_product: Product):
        """Метод для записи новых объектов класса Product в атрибут Category.products"""
        self.__products.append(new_product)
        Category.count_of_goods += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)} шт.\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products
