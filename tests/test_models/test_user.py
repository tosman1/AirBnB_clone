#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import unittest

from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests extended from base_model instantiation for User class."""

    def setUp(self):
        self.user = User()
        self.attr_list = ["email",
                          "password",
                          "first_name",
                          "last_name"]

    def test_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.user, attr)), str)
            self.assertFalse(bool(getattr(self.user, attr)))

    def test_attrs_are_class_attrs(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.user, attr))

    def test_user_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.user), BaseModel))


if __name__ == "__main__":
    unittest.main()
