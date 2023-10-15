#!/usr/bin/python3

""" defines class: Amenities"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """to manage amenities of users"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity clas"""
        super().__init__(*args, **kwargs)
