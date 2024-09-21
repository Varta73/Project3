import pytest
from src.product_category import Category, Product


def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category1.products) == 3

    assert category1.category_count == 2
    assert category2.product_count == 4


def test_product(product):
    assert product.name == "55\" QLED 4K"
    assert product.description == "Фоновая подсветка"
    assert product.price == 123000.0
    assert product.quantity == 7


def test_count_category_products():
    product1 = Product("Iphone 16", "Apple", 180000.0, 5)
    product2 = Product("Galaxy a55", "Samsung", 250000.0, 8)
    category = Category("Смартфоны", "Телефоны для связи", [product1, product2])

    assert Category.product_count == 2
    assert Category.category_count == 1
    assert product1.quantity + product2.quantity == 13


def test_add_product():
    product1 = Product("Товар 3", "Описание товара 3", 200.0, 2)
    product2 = Product("Товар 3", "Описание товара 3", 200.0, 2)
    sum_product = product1.price * product1.quantity + product2.price * product2.quantity

    assert sum_product == 800.0