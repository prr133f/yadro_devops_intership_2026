FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y python3 python3-pip ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY task_01/requirements.txt /app/requirements.txt

RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

COPY task_01/main.py /app/main.py

CMD ["python3", "main.py"]
