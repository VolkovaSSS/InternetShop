def test_product_init(product_test):
    assert product_test.name == "Iphone 15"
    assert product_test.description == "512GB, Gray space"
    assert product_test.price == 210000.0
    assert product_test.quantity == 8
