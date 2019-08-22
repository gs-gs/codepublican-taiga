FROM node:8-alpine

WORKDIR /app/

ARG TAIGA_VERSION

RUN apk update \
    && apk add jq py-pip git\
    && pip install awscli

COPY ./compose/production/events/start /start
RUN chmod ugo+x /start && \
        chown node /start

RUN chown node /app

USER node

RUN git clone https://github.com/taigaio/taiga-events.git /app/
RUN npm install

CMD [ "/start" ]