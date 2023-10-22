from tkinter import Tk, simpledialog, Toplevel, Text
from PIL import Image, ImageDraw, ImageFont
import random

root = Tk()
root.withdraw()
user_input = simpledialog.askstring("Input", "Enter your text:")

if user_input:
    popup = Toplevel(root)
    popup.title("Font-Rendered Output")

    # put list of fonts to use. This is a sample set
    font_choices = ['Arial', 'Times New Roman', 'Courier New', 'Helvetica', 'Verdana']

    for font_name in font_choices:
        try:
            # Attempt to load the font
            font = ImageFont.load_default()
            text_output = Text(popup)
            text_output.insert("1.0", user_input, font)
            text_output.pack()
            break  # If successful, exit the loop
        except Exception as e:
            # Handle any exceptions or errors (e.g., fallback to Arial)
            print(f"Font '{font_name}' failed with error: {e}")
            font = "Arial"
            text_output = Text(popup)
            text_output.insert("1.0", user_input, font)
            text_output.pack()
            break  # Use Arial as a fallback

    popup.wait_window()

root.destroy()
