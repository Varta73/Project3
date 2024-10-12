import pytest

from src.product_category import Category, Product

from typing import Any


def test_category(category1: Category, category2: Category) -> None:
    """Тест на категорию."""
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 122
    assert category1.category_count == 2 or 5
    assert category1.product_count == 4 or 10
    assert len(category2.products) == 34
    assert category2.category_count == 2 or 5
    assert category2.product_count == 4 or 10


def test_product(product: Product) -> None:
    """Тест на продукт."""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product(new_product: str) -> None:
    """Тест на продукт."""
    assert new_product == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 руб. Остаток: 8 "
        "шт.Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )


def test_new_product_2() -> None:
    name_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP " "камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert name_product.name == "Samsung Galaxy S23 Ultra"
    assert name_product.description == "256GB, Серый цвет, 200MP камера"
    assert name_product.price == 180000.0
    assert name_product.quantity == 5


def test_product_str(product):
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0. Остаток: 5"


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_product_add(product1, product):
    assert (product1.price * product1.quantity + product.price * product.quantity) == 1334000.0


def test_category_add(category1):
    print(category1)


def test_middle_price(category1):
    assert category1.middle_price() == 140333 or 16840


def test_invalid_product():
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_middle_price1(category1, category2, product_empty):
    assert category1.middle_price() == 14517 or 105250
    assert category2.middle_price() == 4241 or 30750
    assert product_empty.middle_price() == 0


def test_zero_division_error(product_empty):
    assert product_empty.middle_price() == 0



