FROM alpine:3.7
RUN apk update
RUN apk add wget git python3-dev postgresql postgresql-dev python3 make g++ libxslt-dev libxml2-dev zlib
RUN apk add freetype-dev libjpeg-turbo-dev libpng-dev
RUN apk add linux-headers openldap-dev bash curl yaml-dev file
EXPOSE 8072
EXPOSE 8069
ENV ACCESS_TOKEN=02938974c7dd4aec835dcd86d427f93a
ENV ENVIRONMENT=production
ENV LOCAL_USERNAME=`whoami`
ENV REVISION=`v0.0.1`
RUN curl https://api.rollbar.com/api/1/deploy/ -F access_token=$ACCESS_TOKEN -F environment=$ENVIRONMENT -F revision=$REVISION -F local_username=$LOCAL_USERNAME
RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py; /usr/bin/python3 /tmp/get-pip.py; rm -r /tmp/get-pip.py; ln -sf /usr/bin/pip3 /usr/bin/pip; ln -sf /usr/bin/python3 /usr/bin/python
RUN pip install virtualenv
RUN virtualenv -p /usr/bin/python /srv/.py3
RUN /srv/.py3/bin/pip install lxml==4.1.1
WORKDIR /srv
RUN wget https://github.com/gahan-corporation/gerp/archive/v0.0.1.tar.gz -O /srv/gerp.tar.gz
RUN tar xf gerp.tar.gz; mv /srv/gerp-0.0.1 /srv/gerp;
WORKDIR /srv/gerp
RUN /srv/.py3/bin/python setup.py build
RUN /srv/.py3/bin/python setup.py install
RUN apk add nodejs; npm install -g less
ADD rc /root/.gerprc
ADD gerp /srv/.py3/bin/gerp
RUN chmod +x /srv/.py3/bin/gerp
CMD /srv/.py3/bin/gerp
