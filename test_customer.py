import unittest
from cans import Can, Cola, OrangeSoda, RootBeer
from customer import Customer

class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

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

class TestAddCoinsToWallet(unittest.TestCase):
    """Tests Customer's add_coins_to_wallet method"""

    def setUp(self):
        self.customer = Customer()

    def test_length_of_customers_wallet_money_list_goes_up(self):
        """Testing that the length of the customer's wallet money list goes up"""
        before_count = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet(["quarter","Nickel","Dime"])
        after_count = len(self.customer.wallet.money)
        self.assertEqual(after_count,before_count + 3)

    def test_length_of_customers_wallet_money_list_stays_same(self):
        """Testing that the length of the customer's wallet money list stays
        the same when an empty list passes through it"""
        before_count = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([])
        after_count = len(self.customer.wallet.money)
        self.assertEqual(before_count,after_count)

class TestAddCanToBackpack(unittest.TestCase):
    """Tests Customer's add_can_to_backpack method"""
    
    def setUp(self):
        self.customer = Customer()

    def test_customers_backpacks_purchased_cans_list_goes_up_cola(self):
        """Tests if the Customers backpacks purchased cans list actually goes up"""
        before_count = len(self.customer.backpack.purchased_cans)
        self.customer.backpack.purchased_cans.append(Cola())
        after_count = len(self.customer.backpack.purchased_cans)
        self.assertEqual(after_count,before_count + 1)

    def test_customers_backpacks_purchased_cans_list_goes_up_orange_soda(self):
        """Tests if the Customers backpacks purchased cans list actually goes up"""
        before_count = len(self.customer.backpack.purchased_cans)
        self.customer.backpack.purchased_cans.append(OrangeSoda())
        after_count = len(self.customer.backpack.purchased_cans)
        self.assertEqual(after_count,before_count + 1)

    def test_customers_backpacks_purchased_cans_list_goes_up_root_beer(self):
        """Tests if the Customers backpacks purchased cans list actually goes up"""
        before_count = len(self.customer.backpack.purchased_cans)
        self.customer.backpack.purchased_cans.append(RootBeer())
        after_count = len(self.customer.backpack.purchased_cans)
        self.assertEqual(after_count,before_count + 1)

if __name__ == "__main__":
    unittest.main()