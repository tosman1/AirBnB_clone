#!/usr/bin/python3
"""Test suite for the State class of the models.state module"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        self.state = State()

    def test_name_is_public_class_attribute(self):
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(self.state))
        self.assertNotIn("name", self.state.__dict__)
        # that the name attr is empty
        self.assertFalse(bool(State.name))

    def test_state_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.state), BaseModel))
