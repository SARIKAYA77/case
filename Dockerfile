FROM python:3


# CMD ["gunicorn", "-chdir", "etiya", "--bind", ":8000", "etiya.wsgi:application"]

ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
RUN pip install -r requirements.txt
ADD . /web/
EXPOSE 8000