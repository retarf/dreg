from django.test import TestCase
from rest_framework.test import APIClient

class PullDataViewTestCase(TestCase):
    def test_pull_view_url(self):
        asserted_url = 'http://www.localhost.org'

        client = APIClient()
        response = client.post('/scrubber/pull', {'url': asserted_url}, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['url'], asserted_url)

