#!/usr/bin/python3
"""Test Suite for FileStorage in models/file_storage.py"""
import os.path
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Tests initialization without args"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initializes(self):
        """Tests storage created in __init__.py"""
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Code to execute after tests are executed"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Tests all() method of the FileStorage class"""
        self.assertEqual(dict, type(storage.all()))

        # Tests all() method of the FileStorage class with arg
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """Tests new() method of the FileStorage class"""
        base_model = BaseModel()

        self.assertIn("BaseModel." + base_model.id, storage.all().keys())
        self.assertIn(base_model, storage.all().values())

        # Tests new() method of the FileStorage class with arg
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

        # Tests new() method of the FileStorage class with None
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        """Tests save() method of the FileStorage class"""
        base_model = BaseModel()
        storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)

        # Test with args
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        """Tests the reload method that it works correctly"""
        base_model = BaseModel()
        storage.save()
        storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)

        # check if no file:
        self.assertRaises(FileNotFoundError, storage.reload())

        # Tests the reload method with no args:
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == "__main__":
    unittest.main()
