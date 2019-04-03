FROM python:3.7
WORKDIR /opt/ws
COPY requirements.txt /opt/ws
RUN pip install -r /opt/ws/requirements.txt
