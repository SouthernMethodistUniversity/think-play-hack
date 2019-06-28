FROM rocker/verse:3.5.3

RUN apt-get update \
 && apt-get install -y --no-install-recommends curl gnupg2 \
 && echo "deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main" >> \
    /etc/apt/sources.list.d/pgdg.list \
 && curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
 && apt-get update \
 && apt-get install -y --no-install-recommends postgresql-11 pgadmin4

ENV PATH="/usr/lib/postgresql/11/bin:${PATH}"

