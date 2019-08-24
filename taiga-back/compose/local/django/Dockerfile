FROM python:3.6-alpine3.6

ARG TAIGA_VERSION=4.2.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk update \
    && apk add --virtual build-dependencies \
    # Essentials
    gcc musl-dev libressl-dev \
    # Postgres python client (psycopg2) build dependency
    postgresql-dev \
    # Pillow / PIL build dependencies
    freetype-dev jpeg-dev libwebp-dev tiff-dev libpng-dev lcms2-dev \
    openjpeg-dev zlib-dev libxslt-dev libxml2-dev libffi-dev \
    # Other tools
    git bash

WORKDIR /app

ADD https://github.com/taigaio/taiga-back/archive/${TAIGA_VERSION}.tar.gz ./
    RUN tar -xzf ${TAIGA_VERSION}.tar.gz -C ./ taiga-back-${TAIGA_VERSION} --strip-components=1
RUN rm ${TAIGA_VERSION}.tar.gz

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/extended.txt

COPY ./src/settings/overrides /app/settings/overrides

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r//' /start-flower
RUN chmod +x /start-flower

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
