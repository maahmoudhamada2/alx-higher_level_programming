#!/usr/bin/python3

"""The to_json_string Module"""
import json


def to_json_string(my_obj):
    """Function to return the JSON repr of and object
    Args:
        my_obj: An object to serialized
    Return:
        JSON representation
    """
    return json.dumps(my_obj)
