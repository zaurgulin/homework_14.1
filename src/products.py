class Product:
    """Создан клас продуктов"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
    def price(self) -> float:
        """Геттер для приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для приватного атрибута price"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
            return