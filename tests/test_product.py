from src.product import Product


def test_product_init(product_test):
    assert product_test.name == "Iphone 15"
    assert product_test.description == "512GB, Gray space"
    assert product_test.price == 210000.0
    assert product_test.quantity == 8


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


def test_product_price_setter(capsys, product_test):

    product_test.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_test.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert product_test.price != -100

    product_test.price = 200000.0
    assert product_test.price == 200000.0
