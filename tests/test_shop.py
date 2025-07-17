# tests/test_shop.py

import unittest
from src.shop import SweetShop

class TestSweetShop(unittest.TestCase):

    def setUp(self):
        """
        Setup a fresh sweet shop before each test.
        """
        self.shop = SweetShop()

    def test_get_available_sweets(self):
        self.assertEqual(len(self.shop.get_available_sweets()), 3)

    def test_add_sweet(self):
        self.shop.add_sweet('Jalebi', 15)
        names = [item['name'] for item in self.shop.get_available_sweets()]
        self.assertIn('Jalebi', names)

    def test_remove_sweet(self):
        self.shop.remove_sweet('Barfi')
        names = [item['name'] for item in self.shop.get_available_sweets()]
        self.assertNotIn('Barfi', names)

if __name__ == '__main__':
    unittest.main()
