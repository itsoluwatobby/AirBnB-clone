#!/usr/bin/python3
"""Defines the State modules."""
from models.base_model import BaseModel


class State(BaseModel):
    """stands for a state class for new objects.

    Attributes:
        name (str): name of the state.
    """

    name = ""
