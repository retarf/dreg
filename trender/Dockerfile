FROM        python
ENV         PYTHONBUFFERED 1 
ENV         PYTHONDONTWRITEBYTECODE 1

WORKDIR     /app/trender
COPY        requirements.txt /app/trender
COPY        openssl.cnf /etc/ssl/openssl.cnf

RUN         apt update \
            && apt upgrade -y 

RUN         apt install -y apt-utils python3-setuptools vim pipenv
RUN         pip3 install --upgrade pip -r requirements.txt
RUN         pipenv install
COPY        dev/.ipython /root/.ipython

COPY        . /app/trender

EXPOSE      8000
CMD         gunicorn --bind 0.0.0.0:8000 trender.wsgi
