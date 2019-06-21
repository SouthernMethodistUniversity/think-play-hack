FROM jupyter/datascience-notebook

ARG NB_UID="1000"

USER root

ADD rstudio_auth.sh /usr/lib/rstudio-server/bin/rstudio_auth
ADD ldap_auth.py /usr/lib/rstudio-server/bin/ldap_auth

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates wget gdebi-core libssl1.0.0:amd64 \
 && wget --no-verbose -O rstudio-server.deb \
    "https://download2.rstudio.org/server/trusty/amd64/rstudio-server-1.2.1335-amd64.deb" \
 && gdebi -n rstudio-server.deb \
 && conda install --quiet --yes 'ldap3' \
 && conda clean --all -f -y \
 && fix-permissions $CONDA_DIR \
 && rm -rf /var/lib/apt/lists/* rstudio-server.deb
ENV PATH="${PATH}:/usr/lib/rstudio-server/bin"

USER $NB_UID

