FROM nginx:stable-alpine

ARG TAIGA_VERSION=4.2.13-stable

RUN apk update \
    && apk add jq

WORKDIR /taiga-front-dist
ADD https://github.com/taigaio/taiga-front-dist/archive/${TAIGA_VERSION}.tar.gz ./
RUN tar -xzf ${TAIGA_VERSION}.tar.gz -C ./ taiga-front-dist-${TAIGA_VERSION} --strip-components=1
RUN cp -R  /taiga-front-dist/dist/* /usr/share/nginx/html

COPY ./compose/production/front/entrypoint /entrypoint
RUN chmod ugo+x /entrypoint

WORKDIR /usr/share/nginx/html
ENTRYPOINT [ "/entrypoint" ]
CMD [ "nginx", "-g", "daemon off;"]