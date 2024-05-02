FROM python:3.11


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


WORKDIR /app


COPY req.txt /app/


RUN pip install -r req.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]