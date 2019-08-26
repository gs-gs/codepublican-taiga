FROM nginx:stable-alpine

ARG TAIGA_VERSION=4.2.13-stable
RUN apk update \
    && apk add \
        jq

WORKDIR /taiga-front-dist
ADD https://github.com/taigaio/taiga-front-dist/archive/${TAIGA_VERSION}.tar.gz ./
RUN tar -xzf ${TAIGA_VERSION}.tar.gz -C ./ taiga-front-dist-${TAIGA_VERSION} --strip-components=1


# Install front end plugins 
WORKDIR /taiga-front-dist/dist/plugins
ENV TAIGA_FRONTEND_PLUGINS=""

# -- Github 
WORKDIR /taiga-front-dist/dist/plugins/github-auth/
ARG TAIGA_GITHUB_AUTH_PLUGIN_VERSION=3.1
ENV TAIGA_FRONTEND_PLUGINS="${TAIGA_FRONTEND_PLUGINS}/plugins/github-auth/github-auth.json "
ADD https://github.com/taigaio/taiga-contrib-github-auth/archive/${TAIGA_GITHUB_AUTH_PLUGIN_VERSION}.tar.gz ./
RUN tar -xzf ${TAIGA_GITHUB_AUTH_PLUGIN_VERSION}.tar.gz -C ./ taiga-contrib-github-auth-${TAIGA_GITHUB_AUTH_PLUGIN_VERSION}/front/dist --strip-components=3  && \
    rm ${TAIGA_GITHUB_AUTH_PLUGIN_VERSION}.tar.gz

# -- Slack 
WORKDIR /taiga-front-dist/dist/plugins/slack/
ARG TAIGA_SLACK_PLUGIN_VERSION=3.1
ENV TAIGA_FRONTEND_PLUGINS="${TAIGA_FRONTEND_PLUGINS}/plugins/slack/slack.json "
ADD https://github.com/taigaio/taiga-contrib-slack/archive/${TAIGA_SLACK_PLUGIN_VERSION}.tar.gz ./
RUN tar -xzf ${TAIGA_SLACK_PLUGIN_VERSION}.tar.gz -C ./ taiga-contrib-slack-${TAIGA_SLACK_PLUGIN_VERSION}/front/dist --strip-components=3  && \
    rm ${TAIGA_SLACK_PLUGIN_VERSION}.tar.gz

RUN cp -R  /taiga-front-dist/dist/* /usr/share/nginx/html

COPY ./compose/production/front/entrypoint /entrypoint
RUN chmod ugo+x /entrypoint

# Setup taiga config
RUN rm /etc/nginx/conf.d/*
COPY ./compose/production/front/taiga.conf /etc/nginx/conf.d/taiga.conf

WORKDIR /usr/share/nginx/html
ENTRYPOINT [ "/entrypoint" ]
CMD [ "nginx", "-g", "daemon off;"]