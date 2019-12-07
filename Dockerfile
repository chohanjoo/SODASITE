FROM python:3.6
MAINTAINER jungeun jungeun9729@gmail.com

WORKDIR /home
RUN mkdir SODASITE

WORKDIR ./SODASITE
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD ["python3", "manage.py", "runserver", "0.0.0.0:80"]