#!/usr/bin/python3
"""Defines the class of the City"""
from models.base_model import BaseModel


class City(BaseModel):
    """city class for creating city objects.

    Attributes:
        state_id (str): the state the city is located.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
