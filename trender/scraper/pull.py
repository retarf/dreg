import pandas as pd
import requests
from bs4 import BeautifulSoup


class DataError(Exception):
    pass


class DataPullingError(Exception):
    pass


class Data:

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
