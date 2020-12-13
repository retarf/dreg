FROM        python
ENV         PYTHONBUFFERED 1 
ENV         PYTHONDONTWRITEBYTECODE 1

WORKDIR     /app/scrubber
COPY        requirements.txt /app/scrubber

RUN         apt update \
            && apt upgrade -y 

RUN         apt install -y apt-utils python3-setuptools vim
RUN         pip3 install --upgrade pip -r requirements.txt

COPY        . /app/scrubber

EXPOSE      8000
CMD         gunicorn --bind 0.0.0.0:8000 scrubber.wsgi
