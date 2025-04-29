import pytesseract
from PIL import Image
import numpy as np

def extract_text_from_image(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows path
    text = pytesseract.image_to_string(Image.fromarray(image))
    return text