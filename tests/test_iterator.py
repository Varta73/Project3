import pytest

from src.iterator import ProductIterator

from typing import Any


def test_product_iterator(category1: Any) -> None:
    assert ProductIterator(category1)


def test_product_iterator1(product_iterator: ProductIterator) -> None:
    iter(product_iterator)
    assert product_iterator.index == 2
