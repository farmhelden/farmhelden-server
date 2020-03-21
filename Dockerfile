FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY farmhelden/requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY farmhelden /code/
