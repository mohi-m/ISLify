"""
Utility functions for the ISLify application.
"""

import json
import string

def load_supported_phrases():
    """
    Load supported phrases from a JSON file.

    Returns:
        A list of supported phrases.
    """
    with open("resources/supported_phrases.json", "r") as file:
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
