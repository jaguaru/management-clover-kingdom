FROM python:3.9-slim

WORKDIR /magic_kingdom/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./magic_kingdom/app ./magic_kingdom/app
COPY ./magic_kingdom/app/main.py .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
