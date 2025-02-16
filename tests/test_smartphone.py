import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "Huawei Z230"
    assert smartphone_1.description == "телефон эконом-сегмента"
    assert smartphone_1.price == 5000
    assert smartphone_1.quantity == 315
    assert smartphone_1.efficiency == 6500
    assert smartphone_1.model == "Z230"
    assert smartphone_1.memory == 512
    assert smartphone_1.color == "Черный"


def test_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 5205000


def test_smartphone_add_lawngrass(smartphone_1, lawngrass_1):
    with pytest.raises(TypeError):
        smartphone_1 + lawngrass_1
