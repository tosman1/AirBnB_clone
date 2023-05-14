#!/usr/bin/python3
"""
Unittest suite for base_model __init__.py
"""
import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage


class Teststorage(unittest.TestCase):
    def test_init(self):
        base = BaseModel()
        self.assertEqual(base.__class__, BaseModel)
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
