import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version=1.0)

    def test_get_catalog_items_by(self):
        ids = [1, 2, 3]
        params = self.params_creator.create_catalog_items_by_params(ids)

        response = RequestSender.send_catalog_items_by_get(params)
        self.assertEqual(response.status_code, 200)
