FROM        python
ENV         PYTHONBUFFERED 1 
ENV         PYTHONDONTWRITEBYTECODE 1

WORKDIR     /app/scraper
COPY        requirements.txt /app/scraper
COPY        openssl.cnf /etc/ssl/openssl.cnf

RUN         apt update \
            && apt upgrade -y 

RUN         apt install -y apt-utils python3-setuptools vim 
RUN         pip3 install --upgrade pip -r requirements.txt
COPY        dev/.ipython /root/.ipython

COPY        . /app/scraper

EXPOSE      8001
CMD         uvicorn main:app --reload
