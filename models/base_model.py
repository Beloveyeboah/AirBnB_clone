#!/usr/bin/python3

"""BaseModel established ground for
all common attributes/methods for other classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """ this model Parent class of the Model"""

    def __init__(self, *args, **kwargs):
        """ this method intiate the the Base Class atttribute"""

        if kwargs is not None and kwargs != {}
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """this method converts into strings for
        easy printing"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """this method records and saves the date and time any when
        there is and update"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """this method converts into dictionary for easy
        storrage into json Objects"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict["created_at"].isoformat()
        obj_dict['updated_at'] = obj_dict["updated_at"].isoformat()
        return (obj_dict)
