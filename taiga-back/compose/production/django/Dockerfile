FROM python:3.7-alpine

ARG TAIGA_VERSION=4.2.12

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=settings.production

RUN apk update \
    && apk add --virtual build-dependencies \
    # Essentials
    gcc musl-dev  libressl libressl-dev \
    # Postgres python client (psycopg2) build dependency
    postgresql-dev \
    # Pillow / PIL build dependencies
    freetype-dev jpeg-dev libwebp-dev tiff-dev libpng-dev lcms2-dev \
    openjpeg-dev zlib-dev libxslt-dev libxml2-dev libffi-dev \
    # Other tools
    git

WORKDIR /app

ADD https://github.com/taigaio/taiga-back/archive/${TAIGA_VERSION}.tar.gz ./
    RUN tar -xzf ${TAIGA_VERSION}.tar.gz -C ./ taiga-back-${TAIGA_VERSION} --strip-components=1
RUN rm ${TAIGA_VERSION}.tar.gz

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/extended.txt \
    && rm -rf /extended

COPY ./src/settings/overrides /app/settings/overrides

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown django /start

COPY ./compose/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker
RUN chown django /start-celeryworker

COPY ./compose/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r//' /start-flower
RUN chmod +x /start-flower

COPY . /app

RUN chown -R taiga /app

USER taiga

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
