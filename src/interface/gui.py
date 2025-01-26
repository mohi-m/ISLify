"""
This module handles the graphical user interface for the ISLify application.
"""
import os

import speech_recognition as sr
from easygui import buttonbox

from my_utils import get_resource_dir


def create_main_gui(speech_processor):
    """
    Create and run the main GUI for the ISLify application.

    Args:
        speech_processor: A function to process speech input.
    """
    with sr.Microphone() as source:
        while True:
            image = os.path.join(get_resource_dir(), "signlang.png")
            msg = "HEARING IMPAIRMENT ASSISTANT"
            choices = ["Indian Sign Language", "American Sign Language", "Close"]
            reply = buttonbox(msg, image=image, choices=choices)
            if reply == choices[0]:
                speech_processor(source, "isl")
            if reply == choices[1]:
                speech_processor(source, "asl")
            if reply == choices[2]:
                break
