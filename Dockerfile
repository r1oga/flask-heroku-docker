from continuumio/miniconda3

ADD ./src/requirements.txt /tmp/requirements.txt

RUN pip install -qr /tmp/requirements.txt

ADD ./src /opt/webapp/
WORKDIR /opt/webapp

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
