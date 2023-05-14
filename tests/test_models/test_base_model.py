#!/usr/bin/python3
"""
A module that contains a comprehensive unittest suite for the BaseModel class
"""
import unittest
from time import sleep
from datetime import datetime
from uuid import uuid4

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model.BaseModel
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        Checks that instance has an id assigned on initialization
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, "id"))

    def test_if_id_typeof_is_str(self):
        """
        Checks if id of BaseModel instance is a str object
        """
        b = BaseModel()
        self.assertTrue(type(b.id) is str)

    def test_id_is_unique(self):
        """
        Checks if id of each BaseModel instance is unique
        """
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_created_at_and_updated_at_are_initially_equal(self):
        """
        Checks if create_at == updated_at at initialization
        """
        base_model = BaseModel()
        self.assertEqual(base_model.created_at, base_model.updated_at)

    def test_created_at_is_datetime(self):
        """
        Checks if the attribute 'created_at' is a datetime object
        and that datetime is in isoformat
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.created_at) is datetime)
        # self.assertTrue(base_model.created_at.isoformat())

    def test_updated_at_is_datetime(self):
        """
        Checks that the attribute 'updated_at' is a datetime object
        and that datetime is in isoformat
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.updated_at) is datetime)
        # self.assertTrue(base_model.updated_at.isoformat())

    def test_str_representation(self):
        """
        Checks the BaseModel __str__ representation format
        """
        base_model = BaseModel()
        self.assertEqual(str(base_model),
                         "[BaseModel] ({}) {}".format(base_model.id,
                                                      base_model.__dict__))

    def test_save_works_for_update_at_attr(self):
        """
        Checks if save(self) method updates the updated_at attribute
        """
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, base_model.updated_at)
        self.assertGreater(base_model.updated_at.microsecond,
                           base_model.created_at.microsecond)

    def test_if_to_dict_returns_dict(self):
        """
        Checks if BaseModel.to_dict() returns a dict object
        """
        base_model = BaseModel()
        self.assertTrue(type(base_model.to_dict()) is dict)

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """
        Checks that created_at is stored as a str obj in ISO format
        """
        base_model = BaseModel()
        self.assertEqual(base_model.to_dict()["created_at"],
                         base_model.created_at.isoformat())

    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
        """
        Checks that updated_at is stored as a str obj in ISO format
        """
        base_model = BaseModel()
        self.assertEqual(base_model.to_dict()["updated_at"],
                         base_model.updated_at.isoformat())

    def test_args_unused(self):
        """
        Checks that the attribute 'args' is not used.
        """
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_kwargs_class_key_not_added_as_attribute(self):
        """
        Check that the __class__ key from kwargs is not added as an attribute.
        """
        kwargs = {'__class__': 'TestClass', 'name': 'test_name'}
        base_model = BaseModel(**kwargs)
        self.assertNotIn('__class__', base_model.__dict__)

    def test_if_to_dict_returns_the_accurate_number_of_keys(self):
        """
        Checks that to_dict() returns the expected number of keys/values pairs
        """
        base_model = BaseModel()
        expected_output = {key: value for key, value in
                           base_model.__dict__.items()
                           if not key.startswith("_")}
        self.assertEqual(len(base_model.to_dict()), len(expected_output) + 1)

    def test_when_kwargs_passed_is_empty(self):
        """
        Checks that id, created_at and updated_at are automatically
        generated if they're not in kwargs
        """
        my_dict = {}
        base_model = BaseModel(**my_dict)
        self.assertTrue(type(base_model.id) is str)
        self.assertTrue(type(base_model.created_at) is datetime)
        self.assertTrue(type(base_model.updated_at) is datetime)

    def test_when_kwargs_passed_is_not_empty(self):
        """
        Checks that id, created_at and updated_at are created from kwargs
        """
        my_dict = {"id": uuid4(),
                   "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat()}
        base_model = BaseModel(**my_dict)
        self.assertEqual(base_model.id, my_dict["id"])
        self.assertEqual(base_model.created_at,
                         datetime.strptime(my_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(base_model.updated_at,
                         datetime.strptime(my_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_when_args_and_kwargs_are_passed(self):
        """
        When args and kwargs are passed, BaseModel should ignore args
        """
        date = datetime.now()
        date_iso = date.isoformat()
        base_model = BaseModel("423756",
                               date - datetime.timedelta(minutes=30),
                               "Rahman",
                               id="237689",
                               created_at=date_iso,
                               name="Daniel")
        self.assertEqual(base_model.id, "237689")
        self.assertEqual(base_model.created_at, date)
        self.assertEqual(base_model.name, "Daniel")

    def test_when_kwargs_passed_is_more_than_default(self):
        """
        Checks BaseModel can accept kwargs containing more than
        the default attributes
        """
        my_dict = {"id": uuid4(),
                   "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "first_author": "Daniel Oladele",
                   "second_author": "Oluwatomisin Rahman"}
        base_model = BaseModel(**my_dict)
        self.assertTrue(hasattr(base_model, "first_author"))
        self.assertTrue(hasattr(base_model, "second_author"))

    def test_if_storage_calls_new_method_when_kwargs_is_passed(self):
        """
        Test if storage.new() is called when kwargs is passed to
        the BaseModel
        """
        my_dict = {"id": uuid4(),
                   "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "first_author": "Daniel Oladele",
                   "second_author": "Oluwatomisin Rahman"}
        base_model = BaseModel(**my_dict)
        self.assertTrue(base_model not in models.storage.all().values(),
                        "{}".format(models.storage.all().values()))
        del base_model

        base_model = BaseModel()
        self.assertTrue(base_model in models.storage.all().values())

    def test_if_save_always_updates_when_called(self):
        """
        Tests if save(self) method always updates 'updated_at' when called
        """
        base_model = BaseModel()
        sleep(0.02)
        temp_update = base_model.updated_at
        base_model.save()
        sleep(0.02)
        temp_update1 = base_model.updated_at
        base_model.save()
        sleep(0.02)
        temp_update2 = base_model.updated_at
        self.assertLess(temp_update, temp_update1)
        sleep(0.02)
        base_model.save()
        self.assertLess(temp_update1, temp_update2)
        sleep(0.02)
        base_model.save()
        self.assertLess(temp_update2, base_model.updated_at)

    def test_save_update_file(self):
        """
        Tests if file is updated when the 'save' is called
        """
        base_model = BaseModel()
        base_model.save()
        base_model_id = "BaseModel.{}".format(base_model.id)
        with open("file.json", encoding="utf-8") as f:
            self.assertIn(base_model_id, f.read())

    def test_that_to_dict_contains_correct_keys(self):
        """
        Checks whether to_dict() returns the expected key
        """
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        attrs = ("id", "created_at", "updated_at", "__class__")
        for attr in attrs:
            self.assertIn(attr, base_model_dict)

    def test_to_dict_contains_added_attributes(self):
        """
        Checks that new attributes are also returned by to_dict()
        """
        base_model = BaseModel()
        attrs = ["id", "created_at", "updated_at", "__class__"]
        base_model.name = "Daniel"
        base_model.email = "danieloladele7@gmail.com"
        attrs.extend(["name", "email"])
        for attr in attrs:
            self.assertIn(attr, base_model.to_dict())

    def test_to_dict_output(self):
        """
        Checks the output returned by to_dict()
        """
        base_model = BaseModel()
        date = datetime.now()
        base_model.id = "439086"
        base_model.created_at = base_model.updated_at = date
        test_dict = {
            'id': "439086",
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(test_dict, base_model.to_dict())


if __name__ == "__main__":
    unittest.main()
