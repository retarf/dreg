import pandas as pd

from django.db import models

from scrub.pulling import Web


class Data:

    def __init__(self, url, name):
        self.url = url
        self.name = name

    def serialize(self):
        data = Web(self.url, self.name).data
        data = data.reset_index().drop(columns='index')
        data['Data'] = data['Data'].map(pd.to_datetime)
        data['Wolumen'] = data['Wolumen'].str.replace(" ", "")
        data['Wolumen'] = data['Wolumen'].map(pd.to_numeric)
        data['Obrót'] = data['Obrót'].str.replace(" ", "")
        data['Obrót'] = data['Obrót'].map(pd.to_numeric)

        return data

class WebsiteModel(models.Model):
    url = models.URLField()
