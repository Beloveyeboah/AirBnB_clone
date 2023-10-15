#!/usr/bin/python3

"""defines class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """creates attributes for users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes user class"""
        super().__init__(*args, **kwargs)
