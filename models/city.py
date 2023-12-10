#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """city class contain all data related to city"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
