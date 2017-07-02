import unittest
from functions import *

class FunctionTestCase(unittest.TestCase):
    """Tests for functions.py"""

    def test_say_hello(self):
        """Does say_hello() return the string Hello?"""
        self.assertEqual(say_hello(), "Hello")

    def test_say_hello_is_not_lowercase_or_uppercase(self):
        """say_hello() should not return a hello that is not title case"""
        result = say_hello()
        self.assertNotEqual(result, "hello")
        self.assertNotEqual(result, "HELLO")
        self.assertNotEqual(result, "hElLo")

    def test_return_true_returns_true(self):
        """Does return_true() return True?"""
        self.assertTrue(return_true())

    def test_return_false_returns_false(self):
        """Does return_false() return False?"""
        self.assertFalse(return_false())

    def test_add_to_adds_item_to_list(self):
        """Does add_to() add an item to a list?"""
        my_list = ["a", "b", "c"]
        self.assertNotIn("d", my_list)
        my_list = add_to("d", my_list)
        self.assertIn("d", my_list)

    def test_remove_from_removes_item_from_list(self):
        """Does remove_from() remove an item from a list?"""
        my_list = ["a", "b", "c", "d"]
        self.assertIn("d", my_list)
        my_list = remove_from("d", my_list)
        self.assertNotIn("d", my_list)

unittest.main()
