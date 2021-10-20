import unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """Tests Soda Machine's fill_register method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_length_of_register_list(self):
        """Tests the initial length of the register list"""
        count = len(self.soda_machine.register)
        self.assertEqual(88,count)

class TestFillInventory(unittest.TestCase):
    """Tests Soda Machine's fill_inventory method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_length_of_inventory_list(self):
        count = len(self.soda_machine.inventory)
        self.assertEqual(30,count)

if __name__ == "__main__":
    unittest.main()