#!/usr/bin/python3
"""model create class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseMode"""
    place_id = ""
    user_id = ""
    text = ""
