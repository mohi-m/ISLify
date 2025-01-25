"""
This module handles image and GIF processing for the ISLify application.
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import tkinter as tk
from itertools import count
import string


class ImageLabel(tk.Label):
    """
    A custom Tkinter Label for displaying images and animated GIFs.
    """

    def load(self, im):
        """
        Load an image or animated GIF into the label.

        Args:
            im: Path to the image file or a PIL Image object.
        """
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
        """Unload the current image from the label."""
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        """Display the next frame of an animated GIF."""
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def display_isl_gif(phrase):
    """
    Display an ISL gesture GIF for a given phrase.

    Args:
        phrase: The phrase to display as an ISL gesture.
    """
    root = tk.Tk()
    root.title("ISL Gesture")

    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load(f"resources/isl_gifs/{phrase.lower()}.gif")

    # Update the window to get the correct size
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    position_right = int(screen_width / 2 - window_width / 2)
    position_down = int(screen_height / 2 - window_height / 2)

    # Position the window in the center of the screen
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    # Close the window after 5 seconds
    root.after(5000, root.destroy)

    root.mainloop()


def display_alphabet_images(text):
    """
    Display ISL alphabet images for each character in the given text.

    Args:
        text: The text to display as ISL alphabet images.
    """
    alphabet_list = list(string.ascii_lowercase)

    root = tk.Tk()
    root.title("ISL Alphabet Images")

    lbl = tk.Label(root)
    lbl.pack()

    def show_image(index):
        if index < len(text):
            char = text[index].lower()
            if char in alphabet_list:
                image_path = f"resources/letters/{char}.jpg"
                image = Image.open(image_path)

                # Resize the image to a more manageable size
                image = image.resize((500, 500))

                photo = ImageTk.PhotoImage(image)
                lbl.config(image=photo)
                lbl.image = photo
                root.update_idletasks()

                # Center the window
                window_width = root.winfo_width()
                window_height = root.winfo_height()
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                position_right = int(screen_width / 2 - window_width / 2)
                position_down = int(screen_height / 2 - window_height / 2)
                root.geometry(
                    f"{window_width}x{window_height}+{position_right}+{position_down}"
                )

                root.after(800, show_image, index + 1)
            else:
                root.after(800, show_image, index + 1)
        else:
            root.after(800, root.destroy)

    show_image(0)
    root.mainloop()
