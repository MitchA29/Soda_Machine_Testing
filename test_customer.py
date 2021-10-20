import unittest
from customer import Customer

class TestgetWalletcoin(unittest.TestCase):
    """Tests for the get_wallet_coin method in Customer class"""

    def setUp(self):
        self.customer = Customer()

    def test_quarter_string_returns_quarter_instance(self):
        """Testing that passing in 'Quarter' returns a quarter object"""
        returned_coin = self.customer.get_wallet_coin("Quarter")
        self.assertEqual(.25,returned_coin.value)


if __name__ == "__main__":
    unittest.main()