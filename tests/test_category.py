def test_category_init(first_category, second_category):
    assert first_category.name == "test"
    assert first_category.description == "testing category"
    assert len(first_category.products_in_list) == 2

    assert first_category.count_category == 2
    assert second_category.count_category == 2

    assert first_category.count_of_goods == 4
    assert second_category.count_of_goods == 4


def test_add_product(second_category, product):
    second_category.products = product
    assert len(second_category.products_in_list) == 3

