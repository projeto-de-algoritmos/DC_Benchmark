FROM python:3

WORKDIR benchmark

COPY . .

CMD python3 ./benchmark.py
