#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """class review that contain the data related to review"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

    def __str__(self):
        return "[Review] ({}) {}".format(self.id, self.text)
