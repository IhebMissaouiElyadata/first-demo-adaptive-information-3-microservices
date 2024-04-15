import pytesseract

from PIL import Image


img_file= "../decoded_image.jpg"

img = Image.open(img_file)

ocr_result=pytesseract.image_to_string(img, lang='eng')
print(ocr_result)