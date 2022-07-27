FROM python:3.9.2-alpine

RUN mkdir -p /usr/jobs
WORKDIR /usr/jobs

COPY . .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install requirements.txt