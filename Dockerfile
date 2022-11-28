FROM python:3
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi
