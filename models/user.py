#!/usr/bin/python3
"""importing module"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user contain user details"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
