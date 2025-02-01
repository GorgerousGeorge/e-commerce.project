def test_category_init(first_category, second_category):
    assert first_category.name == "test"
    assert first_category.description == "testing category"
    assert len(first_category.products_in_list) == 2

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_of_goods == 4
    assert second_category.count_of_goods == 4


def test_add_product(second_category, product):
    assert second_category.count_of_goods == 2
    second_category.add_product(product)
    assert second_category.count_of_goods == 3
    assert second_category.products == ('everything, 69.77 руб. Остаток: 13 шт.\n'
                                        'nothing, 100 руб. Остаток: 34435353 шт.\n'
                                        'something, 125.5 руб. Остаток: 666 шт.\n')


def test_products_getter(second_category):
    assert second_category.products == ('everything, 69.77 руб. Остаток: 13 шт.\n'
                                        'nothing, 100 руб. Остаток: 34435353 шт.\n')
