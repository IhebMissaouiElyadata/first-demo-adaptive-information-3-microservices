import base64
from fastapi import HTTPException
from source.schemas.input_data_schema import InputDataSchema
from io import BytesIO
from paddleocr import draw_ocr
import paddleocr
import pytesseract
import io

from PIL import Image


#the order of the four points in each detection box is upper left, upper right, lower right, and lower left.

#Since the detection algorithm in PP-OCR is detected by line, if you want to get the specific coordinates of each word from the detection box coordinates, it will be more difficult.

def optichalCharacterRecognitionPaddle(data: InputDataSchema):
    file_name = data.file_name
    file_type = data.file_type
    print("file name : ", file_name)
    print("file type ", file_type)

    # Decode the base64 data
    image_data_bytes = base64.b64decode(data.file_data)

    # Initialize the PaddleOCR instance
    ocr = paddleocr.PaddleOCR(lang='en', use_gpu=False)
    # Paddleocr supports Chinese, English, French, German, Korean and Japanese.
    # You can set the parameter `lang` as `ch`, `en`, `french`, `german`, `korean`, `japan`
    # to switch the language model in order.
    result = ocr.ocr(image_data_bytes, cls=True)
    #result is a list of list of the desired data
    result = result[0]
    boxes = [line[0] for line in result]
    texts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    return texts, boxes, scores


def optichalCharacterRecognitionTesseract(data: InputDataSchema):
    file_name = data.file_name
    file_type = data.file_type
    # Decode the base
    image_data_bytes = base64.b64decode(data.file_data)
    if not file_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image")
    # Read the image file
    image = Image.open(BytesIO(image_data_bytes))
    try:
        text = pytesseract.image_to_string(image)
    except Exception as e:
        # Handle the exception here, e.g., logging or returning a default value
        print("Error processing image: " + str(e))
        return ""

    return text
