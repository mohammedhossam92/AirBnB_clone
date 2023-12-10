#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """class user contain user details"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def __str__(self):
        return "[User] ({}) {} {}".format(self.id,
                                          self.first_name, self.last_name)
