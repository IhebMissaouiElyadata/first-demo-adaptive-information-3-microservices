import paddleocr

# Install PaddleOCR if not already installed (assuming pip is your package manager)
# uncomment the following line if necessary
# !pip install paddleocr

# Create an OCR object using the desired model (replace 'ppocr_light' with another model if needed)
ocr = paddleocr.PaddleOCR(lang='en', use_gpu=False)  # English, CPU usage (modify as needed)

# Read the image file using OpenCV or Pillow
import cv2

img_path = "/home/iheb/PycharmProjects/ParserMicroservice/ParserMicroservice/decoded_image.jpg" # Replace with your image path
img = cv2.imread(img_path)

# Optionally, pre-process the image (e.g., grayscale conversion) if necessary

# Perform OCR
result = ocr.ocr(img)

# Print the OCR results
for line in result:
    print(line)
    # Access individual elements:
    #   line[0] = list of coordinates (bounding box)
    #   line[1] = recognized text
