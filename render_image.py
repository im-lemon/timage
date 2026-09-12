from PIL import Image
from colorim import Rgb

import os

def render(file: str):
    c = "█"

    img=Image.open(file)
    img=img.convert("RGB")

    t_width = os.get_terminal_size().columns
    img_width = img.width
    img_height = img.height

    scale = t_width / img_width
    new_width = t_width
    new_height = int(img_height * scale * 0.5)

    dims = (new_width, new_height)

    img = img.resize(dims)

    pixels = img.getdata()

    end = []
    for pixel in pixels:
        r,g,b = pixel
        end.append(Rgb.rgb(r, g, b, c))

    for y in range(new_height):
        row = end[y * new_width : (y + 1) * new_width]
        print("".join(row))
    print()