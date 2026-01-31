import pytest

from src.category import Category


def test_category_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации и получения дополнительных функций"
    )
    assert len(first_category.products_in_list) == 2
    assert Category.category_count == 2
    assert Category.product_count == 3
    assert first_category.category_count == 2
    assert first_category.product_count == 3
    assert second_category.category_count == 2
    assert second_category.product_count == 3


def test_category_products_property(first_category):
    assert (
        first_category.products
        == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\nIphone 15, 210000 руб. Остаток: 8 шт.\n"
    )


def test_category_products_setter(first_category, product_test2):
    assert len(first_category.products_in_list) == 2
    first_category.add_product(product_test2)
    assert len(first_category.products_in_list) == 3


def test_category_str(first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 13 шт."


def test_task_iterator(product_iterator_for_test):
    iter(product_iterator_for_test)
    assert product_iterator_for_test.index == 0
    assert next(product_iterator_for_test).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator_for_test).name == "Iphone 15"
    with pytest.raises(StopIteration):
        next(product_iterator_for_test)


def test_category_products_wrong_type(first_category, product_test2):
    with pytest.raises(TypeError):
        first_category.add_product(1)


def test_category_smartphone_setter(first_category, smartphone_test1):
    assert len(first_category.products_in_list) == 2
    first_category.add_product(smartphone_test1)
    assert len(first_category.products_in_list) == 3
    assert first_category.products_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_middle_price(first_category):
    assert first_category.middle_price() == 195000


def test_middle_price_without_products():
    category_without_products = Category(
        "Телевизоры", "Современный телевизор, который позволяет наслаждаться просмотром"
    )
    assert category_without_products.middle_price() == 0
