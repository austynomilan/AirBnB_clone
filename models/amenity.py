#!/usr/bin/python3
"""The amenity class, names the amenities in the place"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name
    """

    name = ""
