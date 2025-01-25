"""
Main entry point for the ISLify application.
This script initializes the speech recognizer and creates the main GUI.
"""

from speech_processor import SpeechRecognizer
from gui import create_main_gui

def main():
    """
    Initialize the application components and start the main GUI.
    """
    speech_recognizer = SpeechRecognizer()
    create_main_gui(speech_recognizer.process_speech)

if __name__ == "__main__":
    main()
