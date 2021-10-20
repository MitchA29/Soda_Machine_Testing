import unittest
from customer import Customer

class TestgetWalletcoin(unittest.TestCase):
    def setUp(self):
        self.customer = Customer()

    def test_quarter_string_returns_quarter_instance(self):
        """Testing that passing in 'Quarter' returns a quarter object"""
        returned_coin = self.customer.get_wallet_coin("Quarter")
        self.assertEqual(.25,returned_coin.value)

    def test_dime_string_returns_dime_instance(self):
        """Testing that passing in 'Dime' returns dime object"""
        returned_coin = self.customer.get_wallet_coin("Dime")
        self.assertEqual(.10,returned_coin.value)

    def test_nickel_string_returns_nickel_instance(self):
        """Testing that passing in 'Nickel' returns nickel object"""
        returned_coin = self.customer.get_wallet_coin("Nickel")
        self.assertEqual(.05,returned_coin.value)

    def test_penny_string_returns_penny_instance(self):
        """Testing that passing in 'Penny' returns penny object"""
        returned_coin = self.customer.get_wallet_coin("Penny")
        self.assertEqual(.01,returned_coin.value)

    def test_not_valid_string_returns_none_instance(self):
        """Testing that passing in a non-valid string returns None"""
        returned_coin = self.customer.get_wallet_coin("Loonie")
        self.assertEqual(None,returned_coin)

if __name__ == "__main__":
    unittest.main()