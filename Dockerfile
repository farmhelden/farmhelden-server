FROM python:3

ADD requirements.txt /opt/

ADD farmhelden /opt/farmhelden

RUN pip install -r /opt/requirements.txt

CMD [ "python", "/opt/farmhelden/manage.py", "runserver" ]



