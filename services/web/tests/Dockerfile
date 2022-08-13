# official base python image
FROM python:3.10.5-bullseye

# working directory 
WORKDIR /usr/src/app/test

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# system dependencies 
# RUN apt-get update && apt-get install -y netcat

# app dependencies
RUN pip install --upgrade pip
RUN pip install pytest requests

COPY . /usr/src/app/test/

RUN pytest -k test_root_url
# entrypoint bash script
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]