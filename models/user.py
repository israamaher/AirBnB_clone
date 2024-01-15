#!/usr/bin/python3
"""model create class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User that inherits from BaseMode"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
