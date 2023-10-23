#!/usr/bin/python3
""" Place module for managing places """
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Place class for creating new Place objects
        Attributes:
            city_id (City.id): id of city where of the Place is
            user_id (User.id): id of user of the Place
            name (str): name of the Place
            description (str): a description of the Place
            number_rooms (int): number of rooms at the Place
            number_bathrooms (int): number of bathrooms at the Place
            max_guest (int): max number of guests can contain the Place
            price_by_night (int): price per night to pay the Place
            latitude (float): latitude of the Place
            longitude (float): longitude of the Place
            amenity_ids (list): list of ids of amenities in the Place
    """
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        if kwargs:
            super(Place, self).__init__(**kwargs)
        else:
            super(Place, self).__init__()
