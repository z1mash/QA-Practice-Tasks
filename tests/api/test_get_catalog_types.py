import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_types(self):
        params = self.params_creator.create_catalog_types_params()

        response = RequestSender.send_catalog_types_get(params)
        self.assertEqual(response.status_code, 200)
