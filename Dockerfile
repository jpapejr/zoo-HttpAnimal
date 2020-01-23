FROM python:3-alpine
LABEL maintainer="John Pape <jpapejr@icloud.com>"

# setup nodemon 
RUN apk add nodejs npm && npm install -g nodemon

COPY requirements.txt /app/requirements.txt
COPY src/main.py /app/main.py

WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP=main.py

ENTRYPOINT [ "/usr/bin/nodemon", "--exec", "flask run", "-e", "py" ]
