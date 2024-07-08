import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_items_by_name(self):
        pageSize = 10
        pageIndex = 0
        name = 'Jacket'  # Замените на нужный name
        params = self.params_creator.create_catalog_items_by_name_params(pageSize, pageIndex, name)

        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)
