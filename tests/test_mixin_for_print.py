from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_mixin_for_print(capsys):
    Product("something", "useful tool for testing", 125.50, 666)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(something, useful tool for testing, 125.5, 666)"

    Smartphone("Huawei Z230", "телефон эконом-сегмента", 5000, 315, 6500,
               "Z230", 512, "Черный")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Huawei Z230, телефон эконом-сегмента, 5000, 315)"

    LawnGrass("Садовая", "газонная трава обычная", 2500, 1000, "Беларусь",
              4, "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Садовая, газонная трава обычная, 2500, 1000)"
