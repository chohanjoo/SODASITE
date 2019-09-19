FROM python:3.6
MAINTAINER jungeun jungeun9729@gmail.com

WORKDIR /home
RUN mkdir SODASITE

WORKDIR ./SODASITE
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]
