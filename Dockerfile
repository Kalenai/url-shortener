FROM python:3.6-stretch

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

# CMD python manage.py runserver -h 0.0.0.0
CMD gunicorn -b 0.0.0.0:5000 wsgi:app
# CMD flask run --host=0.0.0.0