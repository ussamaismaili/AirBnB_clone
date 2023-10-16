#!/usr/bin/python3
"""this Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """this represent city.

    Attributes:
        state_id (str): The state's id.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
