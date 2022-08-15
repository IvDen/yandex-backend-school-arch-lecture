# syntax=docker/dockerfile:1
FROM python:3.10.6-slim-buster
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
# why ETRYPOINTS and CMD didnt work in exec mode?
CMD ["/bin/sh", "-c", "ls"]