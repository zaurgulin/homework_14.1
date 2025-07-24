from src.products import Product


class Category:
    """Класс по описанию категорий"""

    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__products = products

        self.category_count += 1
        self.product_count += len(products) if products else 0

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в атрибут products"""
        self.__products.append(product)

    @property
    def products(self):
        """Метод, который возвращает строку в следующем виде:
        *Название продукта, 80 руб. Остаток: 15 шт.*"""
        for products in self.__products:
            products_srt = f"{products.name}, {products.price} руб. Остаток: {products.quantity} шт.\n"
            return products_srt