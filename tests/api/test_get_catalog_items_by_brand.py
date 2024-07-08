import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_items_by_brand(self):
        pageSize = 10
        pageIndex = 0
        brandId = 1  # Замените на нужный brandId
        params = self.params_creator.create_catalog_items_by_brand_params(pageSize, pageIndex, brandId)

        response = RequestSender.send_catalog_items_by_brand_get(brandId, params)
        self.assertEqual(response.status_code, 200)
