# Please load the image so I can convert it to JPG format for you.

import os
from PIL import Image

# Load the image
input_path = input("Input path to image: ")
head, file_extension = os.path.splitext(input_path)
convert_file = head + "_convert.jpg"

# Open and convert WEBP to JPEG format
def webp():
    image = Image.open(input_path)
    image = image.convert("RGB")  # Ensure it's in RGB mode for JPEG conversion
    image.save(convert_file, "JPEG")

# Open and convert PNG to JPEG format
def png():
	image = Image.open(input_path)
	image = image.convert("RGB")  # Ensure it's in RGB mode for JPEG conversion
	image.save(convert_file, "JPEG")

if file_extension == ".webp":
    webp()
elif file_extension == ".png":
    png()
else:
    print("Unknown file format")
