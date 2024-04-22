
FROM python:3.11.7-slim
WORKDIR /app
COPY ./source/ source/
COPY ./main.py main.py
COPY ./requirements.txt requirements.txt
COPY ./config/ config/
EXPOSE 5000

# Set multiple environment variables
ENV APP_NAME="gatewayapp" \
    PARSER_ENDPOINT="http://localhost:8001/api/parser/ocr/v1/"
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]


