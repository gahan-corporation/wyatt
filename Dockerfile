FROM alpine:latest
RUN apk update
RUN apk add git python3-dev postgresql postgresql-dev python3 py-pip make g++ libxslt-dev libxml2-dev zlib
RUN apk add freetype-dev libjpeg-turbo-dev libpng-dev
RUN pip3 lxml
RUN apk add linux-headers
RUN pip3 install git+https://github.com/gahan-corporation/gerp.git 
