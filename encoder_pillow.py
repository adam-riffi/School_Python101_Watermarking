from PIL import Image
import numpy as np
import sys

def text_to_binary(text):
    """Convert text to a binary string."""
    binary_text = ''
    for char in text:
        binary_text += format(ord(char), '08b')
    binary_text += '1111111111111110'
    return binary_text

def make_pixels_even(image):
    even_image = image.copy()
    even_image = even_image & 0xFE
    return even_image

def encode_text_in_image(image, text):
    binary_text = text_to_binary(text)
    even_image = make_pixels_even(image)
    message_index = 0
    encoded_image = even_image.copy()
    rows, cols, _ = encoded_image.shape

    for row in range(rows):
        for col in range(cols):
            for channel in range(3):
                if message_index < len(binary_text):
                    if  binary_text[message_index] == '1':
                        encoded_image[row, col, channel] |= 1
                    message_index += 1
                else:
                    break
    return encoded_image

def save_image(image, path):
    image.save(path)

# Load the image
img = Image.open('img.png')
img_array = np.array(img)

# Encode text in the image
encoded_array = encode_text_in_image(img_array, "TEST")

# Convert back to PIL Image and save
encoded_img = Image.fromarray(encoded_array.astype('uint8'))
save_image(encoded_img, 'encoded_img.png')