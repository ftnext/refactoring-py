import unittest
from typing import NamedTuple


def price(order):
    base_price = order.quantity * order.item_price
    quantity_discount = max(0, order.quantity - 500) * order.item_price * 0.05
    shipping = min(base_price * 0.1, 100)
    return base_price - quantity_discount + shipping


class PriceTestCase(unittest.TestCase):
    class Order(NamedTuple):
        quantity: int
        item_price: int

    def test_price_parametrize(self):
        for order, expected in [
            # no quantity discount / normal shipping
            (self.Order(quantity=400, item_price=100), 40100),
            # no quantity discount / discounted shipping
            (self.Order(quantity=5, item_price=100), 550),
            # quality discount / normal shipping
            (self.Order(quantity=600, item_price=100), 59600),
            # quality discount / discounted shipping
            (self.Order(quantity=600, item_price=1), 655),
        ]:
            with self.subTest(order=order, expected=expected):
                actual = price(order)

                self.assertEqual(actual, expected)


class Order:
    def __init__(self, a_record) -> None:
        self._data = a_record

    @property
    def quantity(self):
        return self._data.quantity

    @property
    def item_price(self):
        return self._data.item_price

    @property
    def price(self):
        return (
            self.quantity * self.item_price
            - max(0, self.quantity - 500) * self.item_price * 0.05
            + min(self.quantity * self.item_price * 0.1, 100)
        )


if __name__ == "__main__":
    unittest.main()
