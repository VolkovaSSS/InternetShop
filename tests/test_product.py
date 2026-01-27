import pytest

from src.product import Product


def test_product_init(product_test2):
    assert product_test2.name == "Iphone 15"
    assert product_test2.description == "512GB, Gray space"
    assert product_test2.price == 210000.0
    assert product_test2.quantity == 8


def test_new_product():
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_product_price_setter(capsys, product_test2):

    with pytest.raises(ValueError):
        product_test2.price = 0

    with pytest.raises(ValueError):
        product_test2.price = -100

    product_test2.price = 200000.0
    assert product_test2.price == 200000.0


def test_product_str(product_test2):
    assert str(product_test2) == "Iphone 15, 210000 руб. Остаток: 8 шт."


def test_product_add(product_test2: Product, product_test3: Product):
    assert product_test2 + product_test3 == 2114000.0


def test_product_add_wrong_type(product_test2: Product):
    with pytest.raises(TypeError):
        return product_test2 + 1
