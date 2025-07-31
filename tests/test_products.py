from src.products import Product


def test_prod(fixture_product: Product) -> None:
    """Тест свойства объекта Product"""
    assert fixture_product.name == "Samsung Galaxy C23 Ultra"
    assert fixture_product.description == "256GB, Серый цвет, 200MP камера"
    assert fixture_product.price == 180000.0
    assert fixture_product.quantity == 5
    assert fixture_product.__str__() == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_prod_1(fixture_product_1: Product) -> None:
    """Тест свойства объекта Product с другой конфигурацией"""
    assert fixture_product_1.name == "Xiaomi Redmi Note 11"
    assert fixture_product_1.description == "512GB, Черный цвет, 200MP камера"
    assert fixture_product_1.price == 31000.0
    assert fixture_product_1.quantity == 5
    assert fixture_product_1.__str__() == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 5 шт."