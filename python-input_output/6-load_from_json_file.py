#!/usr/bin/python3
"""
This module contains a function to create an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
