FROM python:3.10-slim

WORKDIR /menuapi

RUN pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Cors psycopg2-binary

COPY . .

CMD python server.py