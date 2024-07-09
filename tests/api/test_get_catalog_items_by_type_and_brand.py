import unittest
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


@allure.feature('Catalog Items by Type and Brand Retrieval')
@pytest.mark.get_catalog_items_by_type_and_brand
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Get Catalog Items by Type and Brand')
    @allure.title('Test getting catalog items by type and brand')
    @allure.description('This test verifies the retrieval of catalog items by a specific type and brand.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_catalog_items_by_type_and_brand(self):
        pageIndex = 0
        pageSize = 10
        typeId = 1
        brandId = 1
        params = self.params_creator.create_catalog_items_by_type_and_brand_params(pageIndex, pageSize, typeId, brandId)

        response = RequestSender.send_catalog_items_by_type_and_brand_get(typeId, brandId, params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
        items = response_data.get('data', [])

        for item in items:
            self.assertEqual(item['catalogTypeId'], typeId,
                             f"Item has incorrect catalogTypeId: {item['catalogTypeId']}")
            self.assertEqual(item['catalogBrandId'], brandId,
                             f"Item has incorrect catalogBrandId: {item['catalogBrandId']}")
