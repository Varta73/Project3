from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс, который является родительским для классов продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class PrintMixin:
    """Kласс-миксин, который при создании объекта распечатывает
    в консоль информацию о том, от какого класса и с какими параметрами был создан объект"""

    def __init__(self):
        print(repr(self))
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
