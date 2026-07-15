FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install fastapi uvicorn pydantic cryptography pytest

CMD ["python", "main.py"]
