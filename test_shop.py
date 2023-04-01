import unittest
from shop import shop_items, LeavingStore, Subtraction

class ShopTest(unittest.TestCase):

    def test_item_price(self):
        self.assertEqual(shop_items['socks'], 5)
        self.assertEqual(shop_items['shirt'], 25)
        self.assertEqual(shop_items['bag'], 500)

    def test_LeavingStore(self):
        self.assertRaises(ValueError, LeavingStore('shoes'))
        self.assertEqual(LeavingStore('exit'), None)

    def test_Subtraction(self):
        self.assertEqual(Subtraction(50, 20), 30)
        self.assertEqual(Subtraction(1000, 500), 500)
        self.assertEqual(Subtraction(10, 20), -10)

if __name__ == '__main__':
    unittest.main()
