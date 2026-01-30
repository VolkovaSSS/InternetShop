# import pytest
#
# from src.lawngrass import LawnGrass
# from src.smartphone import Smartphone
#
#
# def test_grass_init(grass_test1):
#     assert grass_test1.name == "Газонная трава"
#     assert grass_test1.description == "Элитная трава для газона"
#     assert grass_test1.price == 500.0
#     assert grass_test1.quantity == 20
#     assert grass_test1.country == "Россия"
#     assert grass_test1.germination_period == "7 дней"
#     assert grass_test1.color == "Зеленый"
#
#
# def test_grass_add(grass_test1: LawnGrass, grass_test2: LawnGrass):
#     assert grass_test1 + grass_test2 == 16750.0
#
#
# def test_grass_add_wrong_type(
#     grass_test1: LawnGrass,
#     smartphone_test1: Smartphone,
# ):
#     with pytest.raises(TypeError):
#         return grass_test1 + smartphone_test1
