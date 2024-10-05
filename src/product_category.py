from typing import Any


class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name: Any, description: Any, price: Any, quantity: Any) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.__price}. Остаток: {self.quantity}"

    def __add__(self: Any, other) -> Any:
        return self.__price * self.quantity + other.__price * other.quantity

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
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        prod: str = ""
        for product in self.__products:
            prod += f"{str(product)}\n"
        return prod
