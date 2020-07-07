FROM python:3.8
#RUN python3 -m venv /opt/venv
ENV PYTHONUNBUFFERED 1
RUN mkdir /carbuddy
WORKDIR /code
COPY requirements.txt /carbuddy/
RUN pip install -r requirements.txt
COPY . /carbuddy/


