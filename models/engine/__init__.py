#!/usr/bin/python3

"""creates package for the file storage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
