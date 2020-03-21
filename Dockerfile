FROM python:3

ADD farmhelden /opt/farmhelden

RUN pip install -r /opt/farmhelden/requirements.txt

CMD [ "python", "/opt/farmhelden/manage.py", "runserver" ]



