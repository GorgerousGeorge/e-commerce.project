from src.product import Product


class Category:
    """Класс для категорий товаров"""
    name: str
    description: str
    products: list
    count_category = 0
    count_of_goods = 0
    total_price: float

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса Category. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = list(products)
        Category.count_category += 1
        Category.count_of_goods += len(products)
        self.total_price = 0
        for product in self.__products:
            self.total_price += (product.quantity * product.price)

    def __str__(self):
        total_goods = 0
        for product in self.__products:
            total_goods += product.quantity
        return f"{self.name}, количество продуктов: {total_goods} шт."

    def __add__(self, other):
        return self.total_price + other.total_price

    def add_product(self, new_product: Product):
        """Метод для записи новых объектов класса Product в атрибут Category.products"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.count_of_goods += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products

    def average_price(self):
        """Метод для подсчета средней цены всех товаров категории"""
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0
