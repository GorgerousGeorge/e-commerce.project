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
    def products_in_string(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products

if __name__ == "__main__":
    product1 = Product("something", "useful tool for testing", 125.50, 666)
    product2 = Product("anything", "everything you desire", 9999999.99, 1)
    product3 = Product("everything", "everything everywhere and at once", 69.77, 13)
    product4 = Product("nothing", "respectfully accepting donations", 100, 34435353)

    Category1 = Category("test", "testing category", [product1, product2, product3])
    print(Category1.products_in_string)
    print(Category1.count_of_goods)
    Category1.add_product(product4)
    print(Category1.products_in_string)
    print(Category1.count_of_goods)