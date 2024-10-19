from typing import Any

from src.base_product import BaseProduct, PrintMixin


class Product(BaseProduct, PrintMixin):
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price}. Остаток: {self.quantity}"

    def __add__(self: Any, other: Any) -> Any:
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict) -> Any:
        new_prod = cls(
            product_dict["name"],
            product_dict["description"],
            product_dict["price"],
            product_dict["quantity"],
        )
        return new_prod

    @property
    def price(self) -> Any:
        return self.__price

    @price.setter
    def price(self, price: Any) -> None:
        if price > 0:
            self.__price = price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: Any, description: Any, products: Any) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        counter = 0
        for product in self.__products:
            counter += product.quantity
        return f"{self.name}, количество продуктов: {counter} шт."

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        prod: str = ""
        for product in self.__products:
            prod += f"{str(product)}\n"
        return prod

    def middle_price(self):
        """Метод, который подсчитывает средний ценник всех товаров"""
        total_price = sum(product.price for product in self.__products)
        try:
            middle_price = total_price / Category.product_count
        except ZeroDivisionError:
            return 0
        return round(middle_price)
