import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
from easygui import *
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
import json


def func(source):
    """
    This function uses speech recognition to listen to the user's speech and translates recognized phrases into
    corresponding Indian Sign Language (ISL) GIFs or alphabet images.
    The function performs the following steps:
    1. Initializes the speech recognizer and microphone.
    2. Calibrates the microphone for ambient noise.
    3. Continuously listens for speech input from the user.
    4. Recognizes the speech using Google Speech Recognition.
    5. If the recognized phrase matches a predefined ISL phrase, it displays the corresponding GIF.
    6. If the recognized phrase contains individual letters, it displays the corresponding alphabet images.
    7. Stops listening and exits if the user says "goodbye", "good bye", or "bye".
    The function handles various exceptions including:
    - Speech recognition errors (e.g., unrecognized speech, request errors).
    - General exceptions during the execution.
    Note:
    - The function uses the `speech_recognition` library for speech recognition.
    - The function uses the `tkinter` library for displaying GIFs.
    - The function uses the `PIL` library for image processing.
    - The function uses the `matplotlib` library for displaying alphabet images.
    """
    recognizer = sr.Recognizer()
    # Load supported phrases from JSON file for which ISL GIFs are available
    with open("supported_phrases.json", "r") as file:
        data = json.load(file)
        supported_phrases = data["phrases"]

    # List of alphabets
    alphabet_list = list(string.ascii_lowercase)

    # Calibrate the microphone for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    print("Please wait. Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=5)

    print("Microphone calibrated. Start speaking.")
    i = 0
    while True:
        print("I am Listening")
        audio = recognizer.listen(source)
        print(audio)
        # recognize speech using Google Speech Recognition
        try:
            rec_audio = recognizer.recognize_google(audio).lower()
            print("You Said: " + rec_audio)

            # Remove punctuation from recognized speech
            translation_table = str.maketrans("", "", string.punctuation)
            rec_audio = rec_audio.translate(translation_table)

            # Stop recording if user says "goodbye", "good bye", or "bye"
            if rec_audio == "goodbye" or rec_audio == "good bye" or rec_audio == "bye":
                print("oops! Time To say good bye")
                break

            # Display ISL GIFs for supported phrases
            elif rec_audio in supported_phrases:

                class ImageLabel(tk.Label):
                    """
                    A Tkinter Label widget that can display images, including animated GIFs.
                    Methods
                    -------
                    load(im):
                        Loads an image or a sequence of images (for animated GIFs) into the label.
                    unload():
                        Unloads the current image from the label.
                    next_frame():
                        Displays the next frame of the image sequence (for animated GIFs).
                    """

                    def load(self, im):
                        if isinstance(im, str):
                            im = Image.open(im)
                        self.loc = 0
                        self.frames = []

                        try:
                            for i in count(1):
                                self.frames.append(ImageTk.PhotoImage(im.copy()))
                                im.seek(i)
                        except EOFError:
                            pass

                        try:
                            self.delay = im.info["duration"]
                        except:
                            self.delay = 100

                        if len(self.frames) == 1:
                            self.config(image=self.frames[0])
                        else:
                            self.next_frame()

                    def unload(self):
                        self.config(image=None)
                        self.frames = None

                    def next_frame(self):
                        if self.frames:
                            self.loc += 1
                            self.loc %= len(self.frames)
                            self.config(image=self.frames[self.loc])
                            self.after(self.delay, self.next_frame)

                root = tk.Tk()
                lbl = ImageLabel(root)
                lbl.pack()
                lbl.load(r"ISL_Gifs/{0}.gif".format(rec_audio.lower()))
                root.mainloop()
            else:
                for i in range(len(rec_audio)):
                    if rec_audio[i] in alphabet_list:

                        ImageAddress = "letters/" + rec_audio[i] + ".jpg"
                        ImageItself = Image.open(ImageAddress)
                        ImageNumpyFormat = np.asarray(ImageItself)
                        plt.imshow(ImageNumpyFormat)
                        plt.draw()
                        plt.pause(0.8)
                    else:
                        continue
        except sr.UnknownValueError:
            print("Google Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Recognition service; {0}".format(
                    e
                )
            )
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            plt.close()


# Entry point of the program
with sr.Microphone() as source:
    while 1:
        image = "signlang.png"
        msg = "HEARING IMPAIRMENT ASSISTANT"
        choices = ["Live Voice", "All Done!"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == choices[0]:
            func(source)
        if reply == choices[1]:
            quit()
