from django.test import TestCase
from rest_framework.test import APIClient

from . import __realdata__

from .pulling import Page

class PullDataViewTestCase(TestCase):
    def test_pull_view_url(self):
        # http://www.localhost.org/nia-historyczne/company,2
        url = 'http://www.localhost.org/historical-data'
        name = 'company'

        client = APIClient()
        data = {
            'url': url,
            'name': name,
        }
        response = client.post('/scrubber/pull', data, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['url'], url)
        self.assertEqual(response.data['name'], name)

class PageTestCase(TestCase):
    def setUp(self):
        self.base_url = __realdata__.url
        self.name = __realdata__.name

    def test_first_page(self):
        page = Page(self.base_url, self.name, 1)
        asserted_url = f'{self.base_url}/{self.name}'
        self.assertEqual(page.url, asserted_url)
        self.assertEqual(page.status_code, 200)

    def test_next_page(self):
        page = Page(self.base_url, self.name, 2)
        asserted_url = f'{self.base_url}/{self.name},2'
        self.assertEqual(page.url, asserted_url)
        self.assertEqual(page.status_code, 200)

    def test_soup(self):
        page = Page(self.base_url, self.name, 2)
        self.assertTrue(__realdata__.name in page.table)

    def test_table(self):
        page = Page(self.base_url, self.name, 1)
        #print(page.table)

