import unittest
from example_class import Customer

class TestCustomer(unittest.TestCase):
    """Tests for classes.py"""

    def setUp(self):
        """Creates instances of Customer to test"""
        self.customer         = Customer("Fred")
        self.paying_customer  = Customer("Sarah", 200)
        self.premium_customer = Customer("Joe King", 500, True)

    def test_init(self):
        """Properly initializes the attributes of a new customer"""
        new_customer = Customer("basic")
        self.assertEqual(new_customer.name, "basic")
        self.assertEqual(new_customer.funbux, 0)
        self.assertEqual(new_customer.premium, False)
        self.assertEqual(len(new_customer.purchase_history), 0)
        another_customer = Customer("has funbux", 500)
        self.assertEqual(another_customer.funbux, 500)
        last_customer = Customer("has premium", 100, True)
        self.assertEqual(last_customer.premium, True)

    def test_buy_funbux(self):
        """A customer can pay to have real money converted to funbux.
        The conversion rate is real_money*10."""
        self.customer.buy_funbux(10)
        self.assertEqual(self.customer.funbux, 100)

    def test_rename_insufficient_funbux(self):
        """If they don't have enough funbux, a customer cannot rename themselves"""
        self.customer.rename("Germ")
        self.assertNotEqual(self.customer.name, "Germ")

    def test_rename_sufficient_funbux(self):
        """If they have enough funbux, a customer can rename themselves"""
        self.paying_customer.rename("Sarabelle")
        self.assertEqual(self.paying_customer.name, "Sarabelle")

    def test_get_premium_insufficient_funbux(self):
        """If they don't have enough funbux, a customer cannot purchase premium status"""
        self.assertFalse(self.customer.premium)
        self.customer.get_premium()
        self.assertFalse(self.customer.premium)

    def test_get_premium_sufficient_funbux(self):
        """If they have enough funbux and aren't already premium, a customer can
        purchase premium status"""
        self.assertFalse(self.paying_customer.premium)
        self.paying_customer.get_premium()
        self.assertTrue(self.paying_customer.premium)

    def test_get_premium_already_premium(self):
        """A customer who is already premium cannot purchase the status again"""
        self.assertTrue(self.premium_customer.premium)
        self.assertEqual(self.premium_customer.get_premium(), "You already have a premium account.")

    def test_end_of_month_enough_for_premium(self):
        """A premium customer that can pay for another month has their status maintained.
        The cost is 100 funbux."""
        self.assertTrue(self.premium_customer.premium)
        funbux_before = self.premium_customer.funbux
        self.premium_customer.end_of_month()
        self.assertTrue(self.premium_customer.premium)
        self.assertEqual(self.premium_customer.funbux, (funbux_before - 100))

    def test_end_of_month_not_enough_for_premium(self):
        """A premium customer that cannot pay for another month has their status revoked.
        To become premium again, they would have to pay the initial fee again."""
        self.assertTrue(self.premium_customer.premium)
        self.premium_customer.funbux = 0
        self.premium_customer.end_of_month()
        self.assertFalse(self.premium_customer.premium)

unittest.main()
