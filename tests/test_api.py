import pytest

from steps.step import *
from classes.Product import *

prod_name = 'Mango'
prod_type = 'FRUIT'
prod_exot = True

prod = Product(prod_name,prod_type,prod_exot)

@pytest.fixture
def product():
    return prod.get_dict() # преобразуем экземпляр в словарь (json)

# тест статуса
def test_check_status():
    assert request_get_check_status() == 200

# тест добавления продукта и проверка
def test_add_product(product):
    assert request_post_add_product(product) == 200
    request_get_all_product()
    assert check_add_product() == product