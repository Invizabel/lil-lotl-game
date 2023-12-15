from PIL import Image
import os

files = os.listdir()
files.sort()
for i in files:
    if i != "image-to-pixel.py" and os.path.isfile(i):
        print(i)
        my_image = Image.open(i)
        pixel_art = my_image.resize((24,24), Image.Resampling.BILINEAR)
        image = pixel_art.resize((24,24), Image.Resampling.NEAREST)
        image.save(i)
