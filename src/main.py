"""
Main entry point for the ISLify application.
This script initializes the speech recognizer and creates the main GUI.
"""

from interface.gui import create_main_gui
from processor.speech_processor import SpeechProcessor


def main():
    """
    Initialize the application components and start the main GUI.
    """
    speech_processor = SpeechProcessor()
    create_main_gui(speech_processor.process_speech)


if __name__ == "__main__":
    main()
