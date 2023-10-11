#!/usr/bin/python3

"""defines class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User:
    """creates attributes for users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
