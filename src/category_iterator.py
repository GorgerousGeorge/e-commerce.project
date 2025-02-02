from src.product import Product
from src.category import Category

class CategoryIterator:
    """Вспомогательный класс для перебора товаров одной категории. Принимает на вход объект класса Category и
    производит итерацию по товарам, которые хранятся в данной категории. Каждая новая итерация возвращает очередной
    товар из категории"""

    def __init__(self, category):
        self.category = category
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
