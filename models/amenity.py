#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """class to define the Amenity"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        return "[Amenity] ({}) {}".format(self.id, self.name)
