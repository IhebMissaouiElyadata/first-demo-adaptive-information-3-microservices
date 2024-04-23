from source.schemas.input_data_schema import InputDataSchema
from source.services.ocr_processor import optichalCharacterRecognitionPaddle


async def request_json_data(input_data:InputDataSchema):
    output_data = {}
    # print(texts)
    texts, boxes, scores = optichalCharacterRecognitionPaddle(input_data)

    # Prepare json response
    output_data['texts'] = texts
    output_data['boxes'] = boxes
    output_data['scores'] = scores
    output_data['instruction'] = input_data.instruction

    return output_data