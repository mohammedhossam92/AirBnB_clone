#!/usr/bin/python3

from models.base_model import BaseModel


class State(BaseModel):
    """class state that contain the data related to class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""

    def __str__(self):
        return "[State] ({}) {}".format(self.id, self.name)
