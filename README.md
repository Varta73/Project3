# Проект "Интернет-магазин"

## Описание:

Проект создан для оптимизации работы в интернет-магазине. Проект разрабатывается на Python в учебных целях и будет (очевидно) дорабатываться.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/Varta73/Project3.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
###### Непонятно что это, но пусть будет
```
python manage.py runserver
```
## Проект содержит:

1. Классы Product и Category.
2. Для класса Product описаны необходимые атрибуты.
3. Для класса Category определены необходимые атрибуты.
4. Для класса Category добавлены два атрибута класса: количество категорий (
category_count) и количество товаров (product_count).
5. Атрибуты класса заполняются автоматически при инициализации нового объекта.
6. Создана функция на подгрузку данных по категориям и товарам из JSON-файла.
7. Для класса Category сделан список товаров приватным атрибутом, чтобы к нему нельзя было получить доступ извне.
8. Для добавления товаров в категорию реализован специальный метод add_product() в классе Category.
9. Для класса Product создан класс-метод new_product, который принимает на вход параметры товара в словаре и возвращает созданный объект класса 
Product.
10. Для класса Product сделан атрибут цены приватным и описаны геттеры и сеттеры.

## Тестирование:
Реализовано тестирование функций проекта через модуль tests.
1. Написаны тесты, которые проверяют корректность инициализации объектов класса Category.
2. Написаны тесты, которые проверяют корректность инициализации объектов класса Product.
3. Написаны тесты, которые проверяют подсчет количества продуктов.
4. Написаны тесты, которые проверяют подсчет количества категорий.
Тестами покрыто 77% кода.

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE)."

![](https://komarev.com/ghpvc/?username=Varta73)