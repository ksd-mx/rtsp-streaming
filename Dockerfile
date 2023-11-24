FROM jrottenberg/ffmpeg:4.4-ubuntu AS builder

RUN apt-get update && apt-get install python3-dev python3-pip -y

FROM builder 

WORKDIR app

COPY ./*.py ./
COPY ./*.txt ./
# COPY ./ffmpeg ./

RUN python3 -m pip install -r requirements.txt