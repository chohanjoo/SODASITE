FROM python:3.6
MAINTAINER jungeun jungeun9729@gmail.com

WORKDIR /home
RUN mkdir SODASITE

WORKDIR ./SODASITE
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["python3", "manage.py", "runserver", "https://endpoint.ainize.ai/jjungeun/sodasite:80"]

# FROM ubuntu:18.04

# RUN apt-get -y update
# RUN apt-get -y dist-upgrade
# RUN apt-get install -y python-pip3 python-dev build-essential

# WORKDIR /home
# RUN mkdir SODASITE

# WORKDIR ./SODASITE
# COPY . .
# RUN pip3 install -r requirements.txt

# EXPOSE 80

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]