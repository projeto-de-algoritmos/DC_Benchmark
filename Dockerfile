FROM python:3

WORKDIR benchmark

RUN apt-get update -y \
    && apt-get install graphviz python-pycallgraph -y

COPY . .

CMD pycallgraph graphviz -- ./benchmark.py
