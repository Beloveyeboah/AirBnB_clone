#!/usr/bin/python3

""" defines class: review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """to manage reviews of users"""

    place_id = ""
    user_id = ""
    text = ""
