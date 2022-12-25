import unittest
from typing import NamedTuple


def price(order):
    # price = base price - quantity discount + shipping
    return (
        order.quantity * order.item_price
        - max(0, order.quantity - 500) * order.item_price * 0.05
        + min(order.quantity * order.item_price * 0.1, 100)
    )


class PriceTestCase(unittest.TestCase):
    class Order(NamedTuple):
        quantity: int
        item_price: int

    def test_no_discount_normal_shipping(self):
        actual = price(self.Order(quantity=100, item_price=400))

        self.assertEqual(actual, 40100)


if __name__ == "__main__":
    unittest.main()
