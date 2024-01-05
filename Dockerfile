FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && \
        apt-get install -y software-properties-common \
        git \
        libx264-dev \
        libv4l-dev \
        v4l-utils \
        ffmpeg \
        python3.11-full \ 
        python3-pip &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /FFVideoStamp

COPY ./requirements.txt requirements.txt
RUN python3.11 -m pip install -r requirements.txt

RUN rm -f /usr/local/bin/python3
RUN ln -s /usr/bin/python3.11 /usr/local/bin/python3

RUN apt-get clean