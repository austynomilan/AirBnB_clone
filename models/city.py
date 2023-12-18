#!/usr/bin/python3
"""City class, encopassing the city instance"""

from models.base_model import BaseModel


class City(BaseModel):
    """A city in the application.

    Attributes:
        name
        state_id
    """
    name = ""
    state_id = ""
