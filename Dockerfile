FROM python:3.8.10
RUN apt-get update
RUN apt-get install python3-opencv -y
COPY requirements.txt /tmp/requirements.txt
COPY main_csv.py /tmp/main_csv.py
RUN python3 -m pip install -r /tmp/requirements.txt