import pytest


def test_category_init(first_category, second_category):
    assert first_category.name == "test"
    assert first_category.description == "testing category"
    assert len(first_category.products_in_list) == 2

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_of_goods == 4
    assert second_category.count_of_goods == 4


def test_add_product(third_category, product):
    assert third_category.count_of_goods == 6
    third_category.add_product(product)
    assert third_category.count_of_goods == 7
    assert third_category.products == ('everything, 69.77 руб. Остаток: 13 шт.\n'
                                       'nothing, 100.00 руб. Остаток: 34435353 шт.\n'
                                       'something, 125.50 руб. Остаток: 666 шт.\n')


def test_products_getter(second_category):
    assert second_category.products == ('everything, 69.77 руб. Остаток: 13 шт.\n'
                                        'nothing, 100.00 руб. Остаток: 34435353 шт.\n')


def test_magick_str_cat(first_category):
    assert str(first_category) == "test, количество продуктов: 667 шт."


def test_magick_add_cat(first_category, second_category):
    assert first_category + second_category == 3453619790


def test_category_iterator(category_iterator):
    assert category_iterator.index == 0
    assert next(category_iterator).name == "something"
    assert next(category_iterator).name == "anything"
    assert category_iterator.index == 2


def test_add_product_incorrect(third_category, second_category):
    with pytest.raises(TypeError):
        third_category.add_product(second_category)
