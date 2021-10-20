import unittest
from unittest.case import TestCase
from coins import Coin
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

class TestDetermineChangevalue(unittest.TestCase):
    """Tests Soda Machine's determine_change_value method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_total_payment_higher(self):
        """Tests if change is correct with total_payment higher"""
        change = self.soda_machine.determine_change_value(5.00,1.00)
        self.assertEqual(4.00,change)

    def test_soda_price_higher(self):
        """Tests if change is correct with soda_price higher"""
        change = self.soda_machine.determine_change_value(1.00,2.00)
        self.assertEqual(-1.00,change)

    def test_prices_equal(self):
        """Tests if change is correct with prices the same"""
        change = self.soda_machine.determine_change_value(1.00,1.00)
        self.assertEqual(0,change)




























































import coins
test_coin_list = []
for index in range(1):
    test_coin_list.append(coins.Quarter())
for index in range(1):
    test_coin_list.append(coins.Dime())
for index in range(1):
    test_coin_list.append(coins.Nickel())
for index in range(1):
    test_coin_list.append(coins.Penny())

class TestDepositIntoRegister(unittest.TestCase):
    """ Test of the deposit into register method of soda machine"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_deposit_coins_into_register(self):
        self.soda_machine.deposit_coins_into_register(test_coin_list)
        print(len(self.soda_machine.register))


if __name__ == "__main__":
    unittest.main()