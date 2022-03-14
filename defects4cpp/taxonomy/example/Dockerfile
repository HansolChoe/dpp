# Copyright 2021 Suresoft Technologies Inc.
# Licensed under the MIT
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3 python3-pip software-properties-common git build-essential bear sudo

RUN pip3 install gcovr
RUN git config --global user.email "minhyuk@suresofttech.com"
RUN git config --global user.name "Peter Kwon"

RUN useradd --uid 1001 --create-home --home-dir /home/workspace --shell /bin/bash defects4cpp
RUN usermod -aG sudo defects4cpp
#USER defects4cpp
ENV USER defects4cpp
WORKDIR /home/workspace
