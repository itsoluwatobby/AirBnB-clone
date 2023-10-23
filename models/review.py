#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for creating new reviews.

    Attributes:
        place_id (str): reviewed place id.
        user_id (str): The id of the User.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
