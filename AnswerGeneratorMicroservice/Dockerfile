FROM python:3.10.12-slim

RUN apt-get update && apt-get install -y tesseract-ocr
WORKDIR /app
COPY ./source/ source/
COPY ./main.py main.py
COPY ./requirements.txt requirements.txt
COPY ./tests/ tests/
COPY ./config/ config/
EXPOSE  5001
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5001"]


