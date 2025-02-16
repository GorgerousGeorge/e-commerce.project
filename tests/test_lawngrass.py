def test_lawngrass_init(lawngrass_1):
    assert lawngrass_1.name == "Садовая"
    assert lawngrass_1.description == "газонная трава обычная"
    assert lawngrass_1.price == 2500
    assert lawngrass_1.quantity == 1000
    assert lawngrass_1.country == "Беларусь"
    assert lawngrass_1.germination_period == 4
    assert lawngrass_1.color == "Зеленый"


def test_lawngrass_add(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 4000000