FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /web
WORKDIR /web
COPY . /web/
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-chdir", "etiya", "--bind", ":8000", "etiya.wsgi:application"]
