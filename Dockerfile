FROM python:3.7-slim

WORKDIR /app

COPY . .

CMD ["python", "test.py"]
