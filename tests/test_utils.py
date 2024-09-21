from unittest.mock import Mock


def test_read_json():
    mock_read_json = Mock(return_value=r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json")
    read_json = mock_read_json
    read_json(file_json=r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json") == r"..\data\products.json"
    mock_read_json.assert_called_once_with(file_json=r"C:\Users\Светлана\PycharmProjects\pythonProject3\data\products.json")