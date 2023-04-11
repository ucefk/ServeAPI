FROM python:3.10-slim-buster

WORKDIR /opt/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ src/
COPY out/ out/
COPY server.py server.py

CMD ["python", "server.py"]
