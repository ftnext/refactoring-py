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


if __name__ == "__main__":
    unittest.main()
