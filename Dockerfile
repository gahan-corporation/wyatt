FROM alpine:latest
RUN apk update
RUN apk add git python3 py-pip make g++ libxslt-dev libxml2-dev zlib
RUN pip3 install git+https://github.com/gahan-corporation/gerp.git 
