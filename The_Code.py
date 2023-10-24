from tkinter import Tk, simpledialog, Toplevel, Text
from PIL import Image, ImageDraw, ImageFont
import random

root = Tk()
root.withdraw()
user_input = simpledialog.askstring("Input", "Enter your text:")

if user_input:
    popup = Toplevel(root)
    popup.title("Font-Rendered Output")

    # put here a list of fonts you want to use. make sure the fonts will work on your operating system!
    font_choices = '''['Font1', 'Font2', 'Font3', 'Font4', 'Font5']'''

    text_output = Text(popup)
    text_output.pack()

    for char in user_input:
        applied_font = False
        for font_name in font_choices:
            try:
                # load attempts
                font = ImageFont.load_default()
                text_output.insert("end", char, font_name)
                applied_font = True
                break  # If successful, exit the loop for character
            except Exception as e:
                # Handle any shenanigans
                print(f"Font '{font_name}' failed with error: {e}")
        
        if not applied_font:
            # If no font applied, use a fallback font (Arial)
            text_output.insert("end", char, "Arial")

    popup.wait_window()

root.destroy()
