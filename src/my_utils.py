"""
Utility functions for the ISLify application.
"""

import json
import os
import string


def load_supported_phrases(type):
    """
    Load supported phrases from a JSON file.

    Returns:
        A list of supported phrases.
    """
    file_path = os.path.join(get_resource_dir(), f"supported_{type}_phrases.json")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No such file or directory: '{file_path}'")
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["phrases"]


def remove_punctuation(text):
    """
    Remove punctuation from the given text.

    Args:
        text: The input text to process.

    Returns:
        The input text with all punctuation removed.
    """
    translation_table = str.maketrans("", "", string.punctuation)
    return text.translate(translation_table)


def get_resource_dir():
    """
    Get the resource directory path relative to the project's base directory.

    Returns:
        The absolute path to the resource directory.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    resource_dir = os.path.join(base_dir, "resources")
    return resource_dir
