## Promt
# act as illustrator
# 1. Repaint this picture in black and white tones with grey gradients.
# 2. Repaint as negative. Black background, white text.

## Solution:
# 1.
# I see you've uploaded an image.
# I've converted the image to black and white with gray gradients while maintaining clarity:

from PIL import Image
import matplotlib.pyplot as plt

# Load the image
input_path = input("Input path to image: ")
out_path = input("Enter directory to output files: ")
image = Image.open(input_path)

# Convert to grayscale
bw_image = image.convert("L")

# Display the processed image
#plt.figure(figsize=(10, 8))
#plt.imshow(bw_image, cmap="gray")
#plt.axis("off")  # Hide axes
#plt.show()

# Save the processed image
bw_image_path = out_path + "/photo_bw.jpg"
bw_image.save(bw_image_path)
bw_image_path

# 2.
# I've converted the image to a negative version with white text on a  black background.

# Convert the grayscale image to a negative (invert colors)
negative_image = Image.eval(bw_image, lambda x: 255 - x)

# Display the processed negative image
#plt.figure(figsize=(10, 8))
#plt.imshow(negative_image, cmap="gray")
#plt.axis("off")  # Hide axes
#plt.show()

# Save the processed negative image
negative_image_path = out_path + "/photo_negative.jpg"
negative_image.save(negative_image_path)
negative_image_path

print("Your redrawn images are contained in the directory", out_path)
