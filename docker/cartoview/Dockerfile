FROM python:2.7.16
LABEL "MAINTAINER"="Cartologic"

# include GDAL HEADER Files
# CPATH specifies a list of directories to be searched as if specified with -I,
# but after any paths given with -I options on the command line.
# This environment variable is used regardless of which language is being preprocessed.
ENV CPATH "$CPATH:/usr/include/gdal:/usr/include"
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
