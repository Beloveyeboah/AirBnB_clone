#!/usr/bin/python3

""" defines class: city"""

from models.base_model import BaseModel


class City(BaseModel):
    """to manage city of users"""

    state_id = ""
    name = ""
