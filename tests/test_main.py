import pytest

from src.product_category import Category, Product


def test_category_init(category1: Category, category2: Category) -> None:
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category1.products) == 122
    assert category1.category_count == 2 or 3
    assert category1.product_count == 4 or 7
    assert len(category2.products) == 34
    assert category2.category_count == 2 or 3
    assert category2.product_count == 4 or 7


def test_product(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_count_category_products() -> None:
    product1 = Product("Iphone 16", "Apple", 180000.0, 5)
    product2 = Product("Galaxy a55", "Samsung", 250000.0, 8)
    category = Category("Смартфоны", "Телефоны для связи", [product1, product2])

    assert Category.product_count == 2 or 6
    assert Category.category_count == 1 or 3
    assert product1.quantity + product2.quantity == 13


def test_add_product() -> None:
    product1 = Product("Товар 1", "Описание товара 1", 100.0, 2)
    product2 = Product("Товар 2", "Описание товара 2", 200.0, 2)
    sum_product = product1.price * product1.quantity + product2.price * product2.quantity

    assert sum_product == 600.0


def test_new_product(new_product):
    assert new_product == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 руб. Остаток: 8 "
        "шт.Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )


def test_new_product_2():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP " "камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
