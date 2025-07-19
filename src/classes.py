from typing import List

class Product:
    """Класс для создания продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для создания категорий"""
    name: str
    description: str
    products: list
    category_count = 0 # Атрибут класса, хранящий количество категорий
    product_count = 0 # Атрибут класса, хранящий общее количество продуктов

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products
        self.product_count += len(products)
        Category.category_count += 1