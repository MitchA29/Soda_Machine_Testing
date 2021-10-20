import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    """Tests Wallet's fill_wallet method"""

    def setUp(self):
        self.wallet = Wallet()

    def test_length_of_wallet(self):
        count = len(self.wallet.money)
        self.assertEqual(88,count)

if __name__ == "__main__":
    unittest.main()