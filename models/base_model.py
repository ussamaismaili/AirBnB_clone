#!/usr/bin/python3
"""BaseModel is a class that encapsulates shared attributes and methods,
serving as a blueprint for other classes. It manages the initialization,
serialization, and deserialization of future instances, ensuring consistent
handling of these aspects.
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    class BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Constructor for the BaseModel class.
        Args:
            *args: Variable number of positional arguments.
            **kwargs: Keyword arguments.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        format = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[key] = datetime.strptime(value, format)
                    else:
                        self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string containing the class name, the object's ID, and its
            attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current timestamp.

        Returns:
            None
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing the object's attributes and the
            "__class__" key with the class name. Datetime objects are
            converted to ISO formatted strings.
        """
        mydict = self.__dict__.copy()
        mydict["__class__"] = self.__class__.__name__
        if not isinstance(mydict["created_at"], str):
            mydict["created_at"] = mydict["created_at"].isoformat()
        if not isinstance(mydict["updated_at"], str):
            mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
