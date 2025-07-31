import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture
def fixture_product() -> Product:
    """Фикстура продукт"""

    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def fixture_product_1() -> Product:
    """Фикстура продукт"""
    return Product("Xiaomi Redmi Note 11", "512GB, Черный цвет, 200MP камера", 31000.0, 5)


@pytest.fixture
def fixture_category() -> Category:
    """Фикстура категории"""
    product_1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product_2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product_3 = Product("Xiaomi Redmi Note 11", "256GB, Серый цвет, 200MP камера", 31000.0, 5)
    return Category("Смартфоны", "Смартфоны, как средство связи", [product_1, product_2, product_3])