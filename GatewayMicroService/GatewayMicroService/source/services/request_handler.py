import httpx
import json
import base64
from fastapi import UploadFile

# if you are transferring binary data between services that support binary data natively, using byte strings may be more efficient. However, if you need to transfer binary data over a text-based protocol or to systems that expect text data, Base64 encoding may be more suitable.
#    return the bytes  as JSON,  so we need to encode them using base64 encoding because bytes string have a problem in utf8 decoding.
async def json_data(file: UploadFile = None, instruction: str = None):
    # Prepare the data to be forwarded
    data = {}

    # Handle file uploads
    if file is not None:
        data["file_name"] = file.filename
        data["file_type"] = file.content_type
        data["file_data"] = base64.b64encode( await file.read()).decode("utf-8")

    if instruction is not None:

        data["instruction"] = instruction
    return data
    # test reconstruction of pdf file
    # import io
    # import PyPDF2
    #
    # # Sample base64 encoded PDF data
    #
    # # Decode base64 data into bytes
    # pdf_bytes = base64.b64decode(data["file_data"])
    #
    # # Create a PDF file from the bytes
    # pdf_file = io.BytesIO(pdf_bytes)
    #
    # # Open the PDF file using PyPDF2
    # pdf_reader = PyPDF2.PdfReader(pdf_file)
    #
    # # Save the PDF file to a new file
    # with open("output_pdf.pdf", "wb") as output_pdf:
    #     pdf_writer = PyPDF2.PdfWriter()
    #     for page_num in range(len(pdf_reader.pages)):
    #         pdf_writer.add_page(pdf_reader.pages[page_num])
    #     pdf_writer.write(output_pdf)

    # Handle text strings

