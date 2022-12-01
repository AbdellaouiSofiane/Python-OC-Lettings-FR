FROM --platform=linux/amd64 python:3.10.1
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app
RUN python3 manage.py collectstatic --no-input
CMD gunicorn --bind 0.0.0.0:$PORT oc_lettings_site.wsgi
