
FROM python:3.11.7-slim
WORKDIR /app
COPY ./source/ source/
COPY ./main.py main.py
COPY ./requirements.txt requirements.txt
COPY ./tests/ tests/
COPY ./config/ config/
EXPOSE  5000
RUN pip install -r requirements.txt
#CMD ["sh", "-c", "pytest tests/test_db.py || true && python main.py"]
#CMD ["sh", "-c", "python exist_tables_or_create.py && uvicorn main:app --host 0.0.0.0 --port 5000"]
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]


