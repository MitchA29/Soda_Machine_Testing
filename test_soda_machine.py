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

if __name__ == "__main__":
    unittest.main()