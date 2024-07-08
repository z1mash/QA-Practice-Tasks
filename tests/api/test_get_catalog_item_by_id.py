import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_item_by_id(self):
        item_id = 1  # или поставить свой
        params = self.params_creator.create_catalog_item_by_id_params(item_id)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 200)
