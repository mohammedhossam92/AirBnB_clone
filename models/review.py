#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """class review that contain the data related to review"""
    place_id = ''
    user_id = ''
    text = ''
