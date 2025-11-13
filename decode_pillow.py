from PIL import Image
import numpy as np
import sys

def binary_to_text(binary_str):
    """Convert a binary string to text."""
    text = ''
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if byte == '11111111':
            if binary_str[i+8:i+16] == '11111110':
                break
        text += chr(int(byte, 2))
    return text

def decode_text_from_image(image):
    binary_text = ''
    rows, cols = image.size

    for row in range(rows):
        for col in range(cols):
            pixel = list(image.getpixel((col, row)))
            for channel in range(3):
                lsb = pixel[channel] & 1
                binary_text += str(lsb)

    text = binary_to_text(binary_text)
    return text


print(decode_text_from_image(Image.open('encoded_img.png')))