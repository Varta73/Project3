import pytest
def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000.0


def test_smartphone_add_error(smartphone1, lawngrass1):
    with pytest.raises(TypeError):
        result = smartphone1 + 1


def test_lawngrass_init(lawngrass1):
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"


def test_lawngrass_add(lawngrass1, lawngrass2):
    assert lawngrass1 + lawngrass2 == 16750.0


def test_lawngrass_add_error(lawngrass1, smartphone1):
    with pytest.raises(TypeError):
        result = lawngrass1 + 1
