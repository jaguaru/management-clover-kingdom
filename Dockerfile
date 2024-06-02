FROM python:3.9-slim

WORKDIR /magic_kingdom/app

ADD . /magic_kingdom/app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "magic_kingdom.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
