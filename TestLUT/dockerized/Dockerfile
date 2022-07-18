FROM python:3.6.1-alpine

RUN mkdir -p /usr/generator
WORKDIR /usr/generator
RUN mkdir -p results
COPY ./GenerateLUTPowerSets.py ./GenerateLUTPowerSets.py
COPY ./network_rules.csv ./network_rules.csv

CMD python3 GenerateLUTPowerSets.py


