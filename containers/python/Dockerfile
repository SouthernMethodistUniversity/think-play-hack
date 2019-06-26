FROM jupyter/datascience-notebook

ARG NB_UID="1000"

USER root

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

USER ${NB_UID}

