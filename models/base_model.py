#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        format = "%Y-%m-%dT%H:%M:%S.%f"
                        self.__dict__[key] = datetime.strptime(key, format)
                    else:
                        self.__dict__[key] = value

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        mydict = self.__dict__
        mydict["__class__"] = self.__class__.__name__
        if not isinstance(mydict["created_at"], str):
            mydict["created_at"] = mydict["created_at"].isoformat()
        if not isinstance(mydict["updated_at"], str):
            mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
