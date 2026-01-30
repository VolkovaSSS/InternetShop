import pytest

from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


def test_smartphone_init(smartphone_test1):
    assert smartphone_test1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_test1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_test1.price == 180000.0
    assert smartphone_test1.quantity == 5
    assert smartphone_test1.efficiency == 95.5
    assert smartphone_test1.model == "S23 Ultra"
    assert smartphone_test1.memory == 256
    assert smartphone_test1.color == "Серый"


def test_smartphone_add(smartphone_test1: Smartphone, smartphone_test2: Smartphone):
    assert smartphone_test1 + smartphone_test2 == 2580000.0


def test_smartphone_add_wrong_type(
    smartphone_test1: Smartphone, grass_test1: LawnGrass
):
    with pytest.raises(TypeError):
        return smartphone_test1 + grass_test1
