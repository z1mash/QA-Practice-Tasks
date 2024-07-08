import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_item_pic_existing(self):
        catalogItemId = 1  # Замените на существующий ID
        params = self.params_creator.create_catalog_item_pic_params(catalogItemId)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 404)
