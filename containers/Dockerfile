FROM jupyter/datascience-notebook

ARG NB_UID="1000"

USER root

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates gnupg2 \
    wget gdebi-core libssl1.0.0:amd64 \
 && wget --no-verbose -O rstudio-server.deb \
    "https://download2.rstudio.org/server/trusty/amd64/rstudio-server-1.2.1335-amd64.deb" \
 && gdebi -n rstudio-server.deb \
 && rm -rf /var/lib/apt/lists/* rstudio-server.deb
ENV PATH="${PATH}:/usr/lib/rstudio-server/bin"

RUN conda install --quiet --yes \
    'nltk' \
    'textblob' \
    'plotly' \
    'seaborn' \
 && conda clean --all -f -y \
 && fix-permissions ${CONDA_DIR} \
 && fix-permissions /home/${NB_USER}

ENV NLTK_DATA /usr/local/share/nltk_data
RUN python3 -m nltk.downloader -d ${NLTK_DATA} all

RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
 && echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" > \
    /etc/apt/sources.list.d/pgdg.list \
 && apt-get update \
 && apt-get install -y --no-install-recommends postgresql-11 pgadmin4

USER ${NB_UID}

