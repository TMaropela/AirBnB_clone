#!/usr/bin/python3
"""Defines our Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representingg an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
