import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from direct_redis import DirectRedis

from dotenv import load_dotenv


class DataError(Exception):
    pass


class DataPullingError(Exception):
    pass


load_dotenv()

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_PANDAS_DB = 0
TIMEZONE = 'Europe/Warsaw'
END_SESSION_HOUR = 17

DATE_FORMAT = '%Y-%M-%d'

DAYS_OF_SESSION_WEEK = "Mon Tue Wed Thu Fri"
redis = DirectRedis(REDIS_HOST, REDIS_PORT, REDIS_PANDAS_DB)
SESSION_WEEK = pd.offsets.CustomBusinessDay(weekmask=DAYS_OF_SESSION_WEEK)

class DataPuller:

    # "https://www.gpw.pl/archiwum-notowan?fetch=0&type=10&instrument=KGHM&date=&show_x=Poka%C5%BC+wyniki"
    url = "https://www.gpw.pl/archiwum-notowan-full"
    params = {
        "fetch": 0,
        "type": 10,
        "date": "",
    }

    def __init__(self, name):
        self.name = name
        self.params["instrument"] = name

    def _get_response(self):
        return requests.get(self.url, self.params)

    def _get_html(self, response):
        if response.status_code != 200:
            raise DataPullingError

        return response.text

    def _get_table(self, html):
        soup = BeautifulSoup(html, "html.parser")
        try:
            table = str(soup.find_all("table")[1])
        except IndexError:
            raise DataPullingError(f"Can't find data for instrument {self.name}")

        return table

    def _get_dataframe(self, table):
        return pd.read_html(table, decimal=",", thousands=" ", index_col=["Data sesji"])[0]

    def _parse_dataframe(self, df):
        df.index = pd.to_datetime(df.index)

        return df

    def get(self):

        response = self._get_response()
        html = self._get_html(response)
        table = self._get_table(html)
        df = self._get_dataframe(table)
        df = self._parse_dataframe(df)

        return df

class Data:

    def __init__(self, company: str):
        self.company = company.upper()

    def get_last_session_date(self) -> pd.Timestamp:
        #TODO: Add days of year without session
        today = pd.Timestamp.today(tz=TIMEZONE)
        last_session = today - 1 * SESSION_WEEK
        if today == today + 0 * SESSION_WEEK and today > today.replace(hour=END_SESSION_HOUR, minute=0, secund=0):
            last_session = today

        return last_session.date()

    def get_data(self):
        df = redis.get(self.company)
        if df is None:
            df = self.pull_data()
        elif not self.get_last_session_date() == df.iloc[-1].name.date():
            df = self.pull_data()
        return df

    def pull_data(self):
        df = DataPuller(self.company).get()
        redis.set(self.company, df)
        return df

    def drop_data(self):
        redis.delete(self.company)