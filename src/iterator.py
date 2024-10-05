from src.product_category import Category, Product

from typing import Any


class ProductIterator:
    def __init__(self, category_prod: Any) -> None:
        self.category = category_prod
        self.index: int = 2

    def __iter__(self):
        self.index = 2
        return self

    def __next__(self):
        if self.category.product_count > self.index:
            prod = self.category.products
            self.index += 1
            return prod
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = ProductIterator(category)

    for product in iterator:
        print(product)
