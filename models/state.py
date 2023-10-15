#!/usr/bin/python3
"""defines class : state"""

from models.base_model import BaseModel


class State(BaseModel):
    """to manage state of users"""

    name = ""

    def __init__(self, *args, **kwargs):
        """ Initialization method """
        super().__init__(*args, **kwargs)
