FROM ubi8
MAINTAINER mail@francescomasala.me
LABEL description="A simple telegram bot in docker"
COPY . /Bot
RUN yum install -y python3-devel gcc && pip3 install -r /Bot/requirements.txt
USER root
ENTRYPOINT ["/usr/python3"]
CMD python3 /Bot/main.py
