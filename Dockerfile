FROM python:3.7.5-buster

ENV PYTHONUNBUFFERED=1 \
    SRC_DIR="/farmhelden"

# take care not to skip it in .dockerignore
RUN apt-get update && \
    apt-get install -y nano \
        postgresql-client \
        binutils \
        libproj-dev \
        gdal-bin && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install aiohttp

RUN mkdir -p ${SRC_DIR}

COPY ./custom-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["custom-entrypoint.sh"]

WORKDIR ${SRC_DIR}
COPY ./farmhelden/requirements.txt ${SRC_DIR}
RUN pip install -r requirements.txt
COPY ./farmhelden ${SRC_DIR}

CMD ["production"]
