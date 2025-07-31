class Product:
    """Создан клас продуктов"""

    name: str
    description: str
    _price: float
    quantity: int

    def __init__(self, name: str, description: str, _price: float, quantity: int):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.price = _price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        product_list_1 = self.quantity * self.price
        product_list_2 = other.price * other.quantity
        total_amount = product_list_1 + product_list_2
        return total_amount

    @classmethod
    def new_product(cls, product):
        """Класс-метод, который принимает на вход параметры товара в словаре и возвращает
        созданный объект класса Product"""
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return Product(name, description, price, quantity)

    @property
    def _price(self) -> float:
        """Геттер для приватного атрибута price"""
        return self._price

    @_price.setter
    def _price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.price = new_price
            return