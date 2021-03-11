import requests
from bs4 import BeautifulSoup
import pandas


class Page:

    def __init__(self, base_url, name, num=0):
        self.base_url = base_url
        self.name = name
        self.num = num
        self.response = requests.get(self.url)

    @property
    def url(self) -> str:
        extension = f'{self.name},{self.num}'
        if self.num <= 1:
            extension = f'{self.name}'
        return f'{self.base_url}/{extension}'

    @property
    def content(self) -> str:
        return self.response.text

    @property
    def status_code(self):
        return self.response.status_code

    @property
    def soup(self):
        return BeautifulSoup(self.content, 'html.parser')

    @property
    def table(self):
        #return self.soup.table
        return self.soup.table

    @property
    def data(self):
        return pandas.read_html(str(self.table))[0]


class Web:

    def __init__(self, webconf, name):
        self.webconf = webconf
        self.url = self.webconf.url
        self.name = name
        self.page = Page(self.url, name)
        self.page_number_class = self.webconf.page_number_class
        self.page_number_separator = self.webconf.page_number_separator

    @property
    def last(self):
        return max([
            int(tag.string)
            for tag in self.page.soup.find_all(class_="pages_pos")
            if tag.string != self.page_number_separator
        ])

    @property
    def data(self):
        return pandas.concat([
            Page(self.url, self.name, page_no).data
            for page_no in range(1, self.last + 1)
        ])
