from heroku/miniconda

ADD src/requirements.txt /tmp/requirements.txt

RUN pip install -qr /tmp/requirements.txt

ADD src/ /opt/webapp
WORKDIR /opt/webapp

CMD python app.py
