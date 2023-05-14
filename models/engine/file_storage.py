#!/usr/bin/python3
"""
A Module for the FileStorage class model
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Represent an abstracted storage engine that serializes instances to
    a JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        self.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        # dump all objdict to .json file
        with open(self.__file_path, mode="w") as f:
            objs = self.__objects
            # save all objects to objdict
            objdict = {key: objs[key].to_dict() for key in objs.keys()}
            json.dump(objdict, f)

    def reload(self):
        """
        Deserialize the JSON file __file_path to __objects, if it exists.
        """
        try:
            with open(self.__file_path) as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
