import cv2
import os
from PIL import Image

def print_all_words(result):
    for sublist in result:
        if isinstance(sublist, list):
            print_all_words(sublist)
        elif isinstance(sublist, tuple):
            word = sublist[0]
            print(word)
image_path = '/home/iheb/PycharmProjects/GatewayMicroService/GatewayMicroService/carte-identite-fr.jpg'

# Load the image
image = Image.open(image_path)

# Initialize the PaddleOCR reader
ocr = paddleocr.PaddleOCR()

# Perform OCR on the image
result = ocr.ocr(image)

print_all_words(result)