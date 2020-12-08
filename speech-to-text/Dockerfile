FROM python:3.9.0

RUN mkdir /usr/src/app/

COPY ./ /usr/src/app/

RUN ls -la /usr/src/app/*

WORKDIR /usr/src/app/

EXPOSE 5000

RUN apt-get update && apt-get install -y ffmpeg

RUN pip install -r requirements.txt

ENV GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/pgcc-aa3647874ba9.json"

CMD [ "python", "app.py" ]
