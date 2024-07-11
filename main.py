import os.path
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Tk
from tkinter import filedialog

from PIL import Image, ImageDraw, ImageFont


def add_watermark():
    user_input = text_entry.get()
    file = filedialog.askopenfilename(initialdir="D:/", title="Upload an image")
    filename = os.path.basename(os.path.splitext(file)[0])
    my_image = Image.open(file).convert("RGBA")
    txt = Image.new("RGBA", my_image.size, (255, 255, 255, 0))
    width, height = my_image.size
    font_size = int(width / 8)
    font = ImageFont.truetype("arial.ttf", font_size)
    d = ImageDraw.Draw(txt)
    x, y = int(width / 2), int(height / 2)
    d.text((x, y), user_input, font=font, fill=(255, 255, 255, 128), anchor="ms")
    image_output = Image.alpha_composite(my_image, txt)
    image_output.show()
    image_output.save(f"{filename}_modified.png")


root = Tk()
root.geometry("320x240")
root.title("Image Watermarking Desktop App")
root.config(bg="black")
watermark_label = Label(root, text="Enter Text for Watermark", bg="black", fg="green", font=("Roboto", 16, "italic"))
watermark_label.pack(pady=10)
text_entry = Entry(root, bg="gray", fg="white", width=30)
text_entry.pack(pady=10)
watermark_button = Button(root, text="Upload your Image", bg="blue", padx=10, pady=5, fg="white", command=add_watermark)
watermark_button.pack(pady=10)
root.mainloop()
