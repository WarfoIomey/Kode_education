FROM python:3.10

WORKDIR /app
ENV PYTHONPATH="${PYTHONPATH}:/app"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y postgresql-client

COPY . .