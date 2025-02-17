from src.product import Product


def test_product_init(product):
    assert product.name == "something"
    assert product.description == "useful tool for testing"
    assert product.price == 125.50
    assert product.quantity == 666


def test_new_product(product, product_in_dict, first_list_products, second_list_products, third_list_products):
    assert product.new_product(product_in_dict, third_list_products).quantity == 14
    assert product.new_product(product_in_dict).name == "everything"
    assert product.new_product(product_in_dict).description == "everything everywhere and at once"
    assert product.new_product(product_in_dict).price == 69.77
    assert product.new_product(product_in_dict).quantity == 13
    assert product.new_product(product_in_dict, first_list_products).name == "everything"
    assert product.new_product(product_in_dict, third_list_products).price == 69.77
    assert product.new_product(product_in_dict, second_list_products).price == 9999999.99


def test_price(capsys, product):
    assert product.price == 125.50
    product.price = 255
    assert product.price == 255
    product.price = -155
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_magick_str(product):
    assert str(product) == "something, 125.50 руб. Остаток: 666 шт."


def test_magick_add(product, second_product):
    assert product + second_product == 84490.01
