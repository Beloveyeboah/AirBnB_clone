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

        if kwargs is not None:
            for key, value in kwargs.item():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.striptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                else:
                    self.__dict = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """this method converts into strings for
        easy printing"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """this method records and saves the date and time any when
        there is and update"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """this method converts into dictionary for easy
        storrage into json Objects"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
