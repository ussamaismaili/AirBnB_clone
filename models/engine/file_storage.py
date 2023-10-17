#!/usr/bin/python3
""" later """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """ The FileStorage class manages the storage and retrieval of data in
    a file, as evident from the save, reload, and new methods
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns all the objects
        stored in the __objects dictionary.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ This method adds a new object to the __objects dictionary.
        """
        id = obj.to_dict()["id"]
        className = obj.to_dict()["__class__"]
        keyName = className + "." + id
        FileStorage.__objects[keyName] = obj

    def save(self):
        """ This method writes the current data in the __objects
        dictionary to the JSON file.
        """
        f_path = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(f_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        f_path = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(f_path):
            try:
                with open(f_path) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "User" in key:
                            data[key] = User(**value)
                        if "Place" in key:
                            data[key] = Place(**value)
                        if "State" in key:
                            data[key] = State(**value)
                        if "City" in key:
                            data[key] = City(**value)
                        if "Amenity" in key:
                            data[key] = Amenity(**value)
                        if "Review" in key:
                            data[key] = Review(**value)
            except Exception:
                pass
