from typing import List, Optional


class Pizza:
    def __init__(self, name: str, toppings: List[str]):
        assert len(name) < 15
        self._name = name
        self._toppings = toppings

    def get_name(self):
        return self._name

    def get_toppings(self):
        return self._toppings

    def set_name(self, name: str):
        assert type(name) is str
        assert len(name) < 15
        self._name = name

    def set_toppings(self, toppings: List[str]):
        assert type(toppings) is list
        self._toppings = toppings

    def add_topping(self, topping: str) -> None:
        if topping not in self._toppings:
            self._toppings.append(topping)
        else:
            raise AssertionError

    def remove_topping(self, topping: str) -> None:
        self._toppings.remove(topping)


class Order:
    _all_orders = []

    def __init__(self):
        self._id = len(Order._all_orders)
        self._pizzas = []
        Order._all_orders.append(self)

    def add_pizza(self, pizza: Pizza) -> None:
        self._pizzas.append(pizza)

    def get_pizzas(self) -> List[Pizza]:
        return self._pizzas

    @classmethod
    def find_order_by_id(cls, id: int) -> Optional['Order']:
        for order in cls._all_orders:
            if order._id == id:
                return order
        return None

    @classmethod
    def get_all_orders(cls) -> List['Order']:
        return cls._all_orders


if __name__ == "__main__":
    import os
    os.system("pytest")
    # os.system("mypy main.py --disallow-untyped-defs")
    # os.system("pycodestyle main.py --ignore=E501,W")
