from rest_framework.test import APITestCase
from rest_framework import status


class SampleTests(APITestCase):

    def test_sample(self):
        http = status.HTTP_200_OK
        url = '/apiv1/'
        res = self.client.get(url)
        self.assertEqual(res.status_code, http)
