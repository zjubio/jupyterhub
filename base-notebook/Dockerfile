FROM tensorflow/tensorflow:latest-py3

LABEL maintainer="Mo Model Team"

USER root

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
# To change the datetime from UTC to Asia/Shanghai
RUN apt-get update && apt-get install -yq graphviz tzdata nano vim wget git python3-tk nodejs pandoc texlive-xetex
# After install node, python2 will be installed
# move back python3 to be default python
#RUN ln -snf /usr/bin/python3 /usr/bin/python
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Configure environment
ENV USR_DIR=/usr \
    LOCAL_DIR=/usr/local \
    SHELL=/bin/bash \
    NB_USER=jovyan \
    NB_UID=1000 \
    NB_GID=100
ENV PATH=$LOCAL_DIR/bin:$PATH \
    HOME=/home/$NB_USER
ENV LANG=C.UTF-8

ADD fix-permissions /usr/local/bin/fix-permissions
# Create jovyan user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
RUN groupadd wheel -g 11 && \
    echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
    useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    mkdir -p $LOCAL_DIR && \
    chown $NB_USER:$NB_GID $LOCAL_DIR && \
    chmod g+w /etc/passwd && \
    fix-permissions $HOME && \
    fix-permissions $LOCAL_DIR

ADD pip.conf /home/jovyan/.pip/pip.conf
RUN chown -R jovyan:users /home/jovyan/.pip

ADD pyls /home/jovyan/pyls
RUN chown -R jovyan:users /home/jovyan/pyls

RUN pip install virtualenvwrapper virtualenv-clone tensorboard==1.11.0

USER $NB_UID

# Setup work directory for backward-compatibility
RUN mkdir /home/$NB_USER/work && \
    fix-permissions /home/$NB_USER

ENV VIRTUALENVWRAPPER_PYTHON $USR_DIR/bin/python3
ENV VIRTUALENVWRAPPER_VIRTUALENV $LOCAL_DIR/bin/virtualenv
SHELL ["/bin/bash", "-c"]

RUN cd /home/jovyan/pyls && npm i && npm run build && cd -

ADD requirements.txt .

RUN source $LOCAL_DIR/bin/virtualenvwrapper.sh && \
#    mkvirtualenv jlenv && \
#    workon jlenv && \
#    pip --default-timeout=100 install jupyterlab==0.31.1 'python-language-server[all]' && \
#    toggleglobalsitepackages && \
    #make basenv
    mkvirtualenv basenv && \
    workon basenv && \
    pip --default-timeout=100 install -U opencv-python nltk notebook seaborn keras Cython && \
    pip --default-timeout=100 install -r requirements.txt && \
    pip --default-timeout=100 install jupyterhub==0.8.1 && \
    pip install http://download.pytorch.org/whl/cu92/torch-0.4.1-cp35-cp35m-linux_x86_64.whl && \
    pip install torchvision && \
    toggleglobalsitepackages

USER root

ADD run.sh /home/jovyan
RUN chown jovyan:users /home/jovyan/run.sh

ADD add_venv.sh /home/jovyan
RUN chown jovyan:users /home/jovyan/add_venv.sh

ADD install_venv.sh /home/jovyan
RUN chown jovyan:users /home/jovyan/install_venv.sh

ADD remove_venv.sh /home/jovyan
RUN chown jovyan:users /home/jovyan/remove_venv.sh

ADD freeze_venv.sh /home/jovyan
RUN chown jovyan:users /home/jovyan/freeze_venv.sh

ADD modules /home/jovyan/modules
RUN chown -R jovyan:users /home/jovyan/modules

ADD dataset /home/jovyan/dataset
RUN chown -R jovyan:users /home/jovyan/dataset

USER $NB_UID

EXPOSE 8888
WORKDIR /home/$NB_USER/work

CMD ['bash', '/home/jovyan/run.sh']
