from typing import Any

from src.product_category import Product


class Smartphone(Product):
    """Класс-наследник Смартфон"""

    def __init__(
        self,
        name: Any,
        description: Any,
        __price: Any,
        quantity: Any,
        efficiency: Any,
        model: Any,
        memory: Any,
        color: Any,
    ) -> None:
        super().__init__(name, description, __price, quantity)
        """Добавляем свойства"""
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    # def __add__(self: Any, other) -> Any:
    #     if isinstance(other, Smartphone):
    #         return (self.__price * self.quantity) + (other.__price * other.quantity)
    #     raise TypeError



if __name__ == "__main__":
    classes = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    print(classes.name)
    print(classes.description)
    print(classes.price)
    print(classes.quantity)
    print(classes.efficiency)
    print(classes.model)
    print(classes.memory)
    print(classes.color)


class LawnGrass(Product):
    """Класс-наследник Газонная трава"""

    def __init__(
        self, name: Any, description: Any, __price: Any, quantity: Any, country: Any, germination_period: Any, color: Any
    ) -> None:
        super().__init__(name, description, __price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    # def __add__(self: Any, other: Any) -> Any:
    #     if type(other) in LawnGrass:
    #         return self.__price * self.quantity + other.__price * other.quantity
    #     raise TypeError


if __name__ == "__main__":
    classes = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    print(classes.name)
    print(classes.description)
    print(classes.price)
    print(classes.quantity)
    print(classes.country)
    print(classes.germination_period)
    print(classes.color)
