import unittest
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


@allure.feature('Catalog Item Retrieval')
@pytest.mark.get_catalog_item
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Get Catalog Item by ID')
    @allure.title('Test getting catalog item by valid ID')
    @allure.description('This test verifies the retrieval of a catalog item by a valid ID.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_catalog_item_by_id(self):
        item_id = 1
        params = self.params_creator.create_catalog_item_by_id_params(item_id)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(response_data['id'], item_id, f"Unexpected item ID: {response_data['id']}")

    @allure.story('Get Nonexistent Catalog Item by ID')
    @allure.title('Test getting catalog item by nonexistent ID')
    @allure.description('This test verifies the retrieval of a catalog item by a nonexistent ID.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_nonexistent_catalog_item_by_id(self):
        nonexistent_item_id = 999999
        params = self.params_creator.create_catalog_item_by_id_params(nonexistent_item_id)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 404, f"Unexpected status code: {response.status_code}")

    @allure.story('Get Catalog Item by Invalid ID')
    @allure.title('Test getting catalog item by invalid ID')
    @allure.description('This test verifies the retrieval of a catalog item by an invalid ID.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_catalog_item_by_invalid_id(self):
        invalid_item_id = -1
        params = self.params_creator.create_catalog_item_by_id_params(invalid_item_id)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 400, f"Unexpected status code: {response.status_code}")
