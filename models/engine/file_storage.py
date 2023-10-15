#!/usr/bin/python3
""" later """
import json
import os
from models.base_model import BaseModel


class fileStorage:
	""" The FileStorage class manages the storage and retrieval of data in a file,
		as evident from the save, reload,
 		and new methods 
	"""

	__file_path = "file.json"
	__all_objects = {}
	
	def all(self):
	""" this method returns all the objects stored in the __all_objects dictionary. """
		return fileStorage.__all_objects

	def new(self, obj):
	""" this method adds a new object to the __all_objects dictionary """
		id = obj.to_dict()["id"]
		className = obj.to_dict()["__class__"]
		keyName = className+"."+id
		fileStorage.__all_objects[keyName] = obj

	def save(self):
	""" this method writes the current data in the __all_objects dictionary to the JSON file """
		filepath = fileStorage.__file_path
		data = dict(fileStorage.__all_objects)
		for key, value in data.items():
		data[key] = value.to_dict()
		with open(filepath, 'w') as f:
		json.dump(data, f)

"""	def reload(self): """

