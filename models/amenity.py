#!/usr/bin/python3
"""to Define the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """this Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
