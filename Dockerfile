FROM python:3.6-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=manage.py

# EXPOSE 80

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
