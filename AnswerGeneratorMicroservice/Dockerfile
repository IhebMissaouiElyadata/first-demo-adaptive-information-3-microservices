FROM python:3.10.12-slim

RUN apt-get update && apt-get install -y tesseract-ocr
WORKDIR /app
COPY ./source/ source/
COPY ./main.py main.py
COPY ./requirements.txt requirements.txt
COPY ./config/ config/
EXPOSE  5000
# Set multiple environment variables
ENV APP_NAME="answer_gen_APP" \
    answer_gen_APP="https://3aca-35-247-170-134.ngrok-free.app/post"
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]


