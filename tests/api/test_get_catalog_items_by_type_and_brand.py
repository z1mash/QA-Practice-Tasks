import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_items_by_type_and_brand(self):
        pageIndex = 0
        pageSize = 10
        typeId = 1
        brandId = 1
        params = self.params_creator.create_catalog_items_by_type_and_brand_params(pageIndex, pageSize, typeId, brandId)

        response = RequestSender.send_catalog_items_by_type_and_brand_get(typeId, brandId, params)
        self.assertEqual(response.status_code, 200)
