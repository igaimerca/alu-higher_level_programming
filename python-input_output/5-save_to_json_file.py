#!/usr/bin/python3
"""
This module contains a function to write an object to a text file using
a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to serialize to JSON.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
