FROM python:3.8-slim

COPY . /app

RUN pip3 install flask requests

WORKDIR /app

ENTRYPOINT [ "python", "app.py" ]