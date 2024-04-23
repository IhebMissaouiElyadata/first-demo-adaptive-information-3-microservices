FROM python:3.10.12-slim
# Install system dependencies

RUN apt-get update && apt-get install -y libgl1-mesa-glx && apt-get install -y  libgomp1 libglib2.0-0

#RUN apt-get  install -y tesseract-oc

WORKDIR /app
COPY ./source/ source/
COPY ./main.py main.py
COPY ./requirements.txt requirements.txt
COPY ./config/ config/
EXPOSE  5000
# Set multiple environment variables
ENV APP_NAME="parser" \
    ANS_GEN_ENDPOINT="http://localhost:8004/api/answerGenerator/LLM/v1/"
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]


