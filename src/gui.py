"""
This module handles the graphical user interface for the ISLify application.
"""

from easygui import buttonbox
import speech_recognition as sr

def create_main_gui(speech_processor):
    """
    Create and run the main GUI for the ISLify application.

    Args:
        speech_processor: A function to process speech input.
    """
    with sr.Microphone() as source:
        while True:
            image = "signlang.png"
            msg = "HEARING IMPAIRMENT ASSISTANT"
            choices = ["Live Voice", "All Done!"]
            reply = buttonbox(msg, image=image, choices=choices)
            if reply == choices[0]:
                speech_processor(source)
            if reply == choices[1]:
                break
