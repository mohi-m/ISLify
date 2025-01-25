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
    lbl = ImageLabel(root)
    lbl.pack()
    lbl.load(f"ISL_Gifs/{phrase.lower()}.gif")
    
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
    for char in text:
        if char in alphabet_list:
            image_path = f"letters/{char}.jpg"
            image = Image.open(image_path)
            image_array = np.asarray(image)
            plt.imshow(image_array)
            plt.draw()
            plt.pause(0.8)
    plt.close()
