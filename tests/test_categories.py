from src.categories import Category
from src.products import Product


def test_prod(fixture_product: Product, fixture_category: Category) -> None:
    """Тест свойств объекта Category и Product"""
    fixture_category.__products = [fixture_product]
    assert fixture_category.name == "Смартфоны"
    assert fixture_category.description == "Смартфоны, как средство связи"
    # assert fixture_category.products[0].price == 180000.0
    # assert fixture_category.products[0].name == "Samsung Galaxy C23 Ultra"
    # assert fixture_category.products[0].description == "256GB, Серый цвет, 200MP камера"
    # assert fixture_category.products[0].quantity == 5
    assert fixture_category.category_count == 1
    assert fixture_category.product_count == 3
    assert fixture_category.__str__() == "Смартфоны, количество продуктов: 18 шт."


def test_category_products_property(fixture_category: Category) -> None:
    """Тестируем геттер, который возвращает строку со всеми продуктами в приватном атрибуте products"""
    assert fixture_category.products == (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        # "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        # "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )