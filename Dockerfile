FROM alpine:3.7
RUN apk update
RUN apk add git python3-dev postgresql postgresql-dev python3 py-pip make g++ libxslt-dev libxml2-dev zlib
RUN apk add freetype-dev libjpeg-turbo-dev libpng-dev
RUN pip3 install lxml==4.1.1
RUN apk add linux-headers openldap-dev bash
RUN pip3 install https://github.com/gahan-corporation/gerp/archive/v0.0.1.tar.gz 
