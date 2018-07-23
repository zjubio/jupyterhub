#!/usr/bin/env bash
M_DIR=/home/jovyan/work
REQ_TXT=/home/jovyan/work/faas_requirements.txt

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh

# create module env
export WORKON_HOME=${M_DIR}
mkvirtualenv mynewenv
# install packages
pip install -r ${REQ_TXT}