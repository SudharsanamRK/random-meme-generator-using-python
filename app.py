import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
import random

# === CONFIG ===
MEME_FOLDER = 'memes'
FONT_PATH = 'fonts/Impact.ttf'  # Use a fallback font if this is missing
TEXT_FILE = 'texts.txt'
DISPLAY_SIZE = (500, 500)  # Resize all memes to fit this

# === Load Captions ===
with open(TEXT_FILE, 'r', encoding='utf-8') as f:
    captions = [line.strip() for line in f if line.strip()]

# === Main App ===
class MemeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Meme Generator")

        self.img_label = tk.Label(root)
        self.img_label.pack(padx=10, pady=10)

        self.next_btn = tk.Button(
            root, text="Next Meme", command=self.show_random_meme,
            bg="#1e90ff", fg="white", font=("Arial", 12, "bold")
        )
        self.next_btn.pack(pady=(0, 10))

        self.show_random_meme()

    def show_random_meme(self):
        # Pick image and caption
        meme_path = os.path.join(MEME_FOLDER, random.choice(os.listdir(MEME_FOLDER)))
        caption = random.choice(captions)

        # Open and resize image
        img = Image.open(meme_path).convert("RGB")
        img = img.resize(DISPLAY_SIZE, Image.LANCZOS)

        # Draw caption on image
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype(FONT_PATH, 28)
        except:
            font = ImageFont.load_default()

        # Draw text on bottom center
        bbox = draw.textbbox((0, 0), caption, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (img.width - text_width) / 2
        y = img.height - text_height - 10
        draw.text((x, y), caption, font=font, fill='white', stroke_fill='black', stroke_width=2)

        # Show in Tkinter
        self.tk_img = ImageTk.PhotoImage(img)
        self.img_label.config(image=self.tk_img)

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = MemeApp(root)
    root.mainloop()
