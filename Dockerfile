FROM python:3.8-slim-bullseye

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y awscli

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
