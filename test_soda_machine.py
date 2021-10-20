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
        """Tests the initial length of the inventory list"""
        count = len(self.soda_machine.inventory)
        self.assertEqual(30,count)

class TestGetCoinFromRegister(unittest.TestCase):
    """Tests Soda Machine's get_coin_from_register method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_return_quarter_from_register(self):
        """Tests that its possible to return a quarter from register"""
        returned_coin = self.soda_machine.get_coin_from_register("Quarter")
        self.assertEqual(.25,returned_coin.value)

    def test_return_dime_from_register(self):
        """Tests that its possible to return a dime from register"""
        returned_coin = self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(.1,returned_coin.value)

    def test_return_nickel_from_register(self):
        """Tests that its possible to return a nickel from register"""
        returned_coin = self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(.05,returned_coin.value)

    def test_return_penny_from_register(self):
        """Tests that its possible to return a penny from register"""
        returned_coin = self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(.01,returned_coin.value)

    def test_return_none_from_register(self):
        """Tests that when invalid option, returns none from register"""
        returned_coin = self.soda_machine.get_coin_from_register("Loonie")
        self.assertEqual(None,returned_coin)

class TestRegisterHasCoin(unittest.TestCase):
    """Tests Soda Machine's register_has_coin method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_return_quarter_is_true(self):
        """Tests if a quarter is in register"""
        coin = self.soda_machine.register_has_coin("Quarter")
        self.assertTrue(coin)

    def test_return_dime_is_true(self):
        """Tests if a dime is in register"""
        coin = self.soda_machine.register_has_coin("Dime")
        self.assertTrue(coin)

    def test_return_nickel_is_true(self):
        """Tests if a nickel is in register"""
        coin = self.soda_machine.register_has_coin("Nickel")
        self.assertTrue(coin)

    def test_return_penny_is_true(self):
        """Tests if a penny is in register"""
        coin = self.soda_machine.register_has_coin("Penny")
        self.assertTrue(coin)

    def test_return_non_vailid_is_false(self):
        coin = self.soda_machine.register_has_coin("Loonie")
        self.assertFalse(coin)


if __name__ == "__main__":
    unittest.main()