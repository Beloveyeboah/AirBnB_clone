#!/usr/bin/python3

"""creats and initializes the package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
