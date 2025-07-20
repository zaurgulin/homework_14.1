import pytest
from src.classes import Product, Category

@pytest.fixture
def product():
    return Product(name="Товар", description="Описание товара", price=100.50, quantity=10)

@pytest.fixture
def category():
    return Category(name="Категория", description="Описание категории", products=[])

def test_product_initialization(product):
     assert product.name == "Товар"
     assert product.description == "Описание товара"
     assert product.price == 100.50
     assert product.quantity == 10

def test_category_initialization(category):
     assert category.name == "Категория"
     assert category.description == "Описание категории"
     assert isinstance(category.products, list)
     assert len(category.products) == 0

# def test_class_attributes_initialization():
#      assert Category.category_count == 0
#      assert Category.category_count == 1
#      assert Category.product_count == 0