FROM alpine:latest
RUN apk update
RUN apk add python3 py-pip3 make g++ libxslt-dev libxml2-dev zlib
