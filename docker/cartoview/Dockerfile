FROM python:3.8.3
LABEL "MAINTAINER"="Cartologic"

ENV PYTHONUNBUFFERED 1

ARG APP_DIR=/usr/src/carto_app

COPY ./scripts/ /cartoview_scripts/
WORKDIR /scripts
RUN chmod +x /cartoview_scripts/*
RUN /cartoview_scripts/setup.sh
RUN rm -rf /cartoview_scripts

RUN mkdir -p ${APP_DIR}
VOLUME ${APP_DIR}
WORKDIR ${APP_DIR}

CMD ["/bin/bash"]
