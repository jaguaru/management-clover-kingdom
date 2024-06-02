FROM python:3.9-slim

WORKDIR /magic_kingdom/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/magic_kingdom/app

EXPOSE 8000

CMD ["uvicorn", "magic_kingdom.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
