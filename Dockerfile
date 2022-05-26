FROM ubuntu:20.04

WORKDIR /moonseacodex_api
COPY . /moonseacodex_api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ=Europe/London

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install python external libs, and web server packages
RUN apt update && apt install python3 python3-pip python3-venv apache2 libapache2-mod-wsgi-py3 libpq-dev -y

# Create python virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Update tooling and install required packages
RUN pip install --upgrade pip setuptools wheel && pip install -r requirements.txt
# Enable site
RUN mv /moonseacodex_api/deploy/api.conf /etc/apache2/sites-available/api.conf && a2ensite api

CMD ["apachectl", "-D",  "FOREGROUND"]
