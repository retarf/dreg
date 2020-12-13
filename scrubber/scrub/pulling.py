import requests

class Page:

    def __init__(self, base_url, name, num):
        self.base_url = base_url
        self.name = name
        self.num = num

    @property
    def url(self) -> str:
        extension = f'{self.name},{self.num}'
        if self.num <= 1:
            extension = f'{self.name}'
        return f'{self.base_url}/{extension}'

    @property
    def response(self):
        return requests.get(self.url)

    @property
    def content(self):
        return self.response.text

    @property
    def status_code(self):
        return self.response.status_code




