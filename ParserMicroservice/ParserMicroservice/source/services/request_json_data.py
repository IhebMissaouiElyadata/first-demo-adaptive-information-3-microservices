from source.schemas.input_data_schema import InputDataSchema
from source.services.ocr_processor import optichalCharacterRecognitionPaddle


async def request_json_data(input_data:InputDataSchema):
    output_data = {}
    # texts =  optichalCharacterRecognitionTesseract(data)
    # print(texts)
    texts, boxes, scores = optichalCharacterRecognitionPaddle(input_data)
    #print(boxes[0])
    #print(texts[0])
    #print(scores[0])
    # Prepare json response
    output_data['texts'] = texts
    output_data['boxes'] = boxes
    output_data['scores'] = scores
    output_data['instruction'] = input_data.instruction

    return output_data