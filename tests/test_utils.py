from unittest.mock import Mock, mock_open, patch

import pytest

from src.utils import read_json

from typing import Any


def test_read_json() -> None:
    mock_read_json = Mock(return_value=r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json")
    read_json = mock_read_json
    read_json(
        file_json=r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json"
    ) == r"..\data\products.json"
    mock_read_json.assert_called_once_with(
        file_json=r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json"
    )


def test_read_json1() -> None:
    """Тест ошибки при считывании файла"""
    with pytest.raises(Exception) as f:
        read_json(" ")
        assert str(f.value) == "При считывании файла произошла ошибка."


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_json2(tmp_path: Any) -> None:
    """Тест на пустой файл"""
    prod = read_json("data/products.json")
    assert prod == []
