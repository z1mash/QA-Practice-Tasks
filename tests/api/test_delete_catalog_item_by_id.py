import unittest
import random
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


@allure.feature('Catalog Item Management')
@pytest.mark.delete_catalog_item
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Create and Delete Catalog Item')
    @allure.title('Test creating and deleting a catalog item')
    @allure.description('This test verifies the creation and deletion of a catalog item.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_create_and_delete_catalog_item(self):
        unique_id = random.randint(10000, 99999)

        post_data = {
            'id': unique_id,
            'name': 'Test Item',
            'description': 'This is a test item',
            'price': 100,
            'pictureFileName': 'test.jpg',
            'catalogTypeId': 1,
            'catalogBrandId': 1,
            'availableStock': 10,
            'restockThreshold': 5,
            'maxStockThreshold': 20,
            'onReorder': False
        }
        create_params = self.params_creator.create_catalog_items_post_params(post_data)
        create_response = RequestSender.send_catalog_items_post(create_params)
        self.assertEqual(create_response.status_code, 201)

        delete_params = self.params_creator.create_delete_catalog_item_by_id_params(unique_id)
        delete_response = RequestSender.send_delete_catalog_item_by_id(delete_params)
        self.assertEqual(delete_response.status_code, 204)

        get_params = self.params_creator.create_catalog_item_by_id_params(id=unique_id)
        get_response = RequestSender.send_catalog_item_by_id_get(get_params)
        self.assertEqual(get_response.status_code, 404, f"Unexpected status code: {get_response.status_code}")

    @allure.story('Delete Non-Existing Catalog Item')
    @allure.title('Test deleting a non-existing catalog item')
    @allure.description('This test verifies the deletion of a non-existing catalog item.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_non_existing_catalog_item(self):
        item_id = 9999
        params = self.params_creator.create_delete_catalog_item_by_id_params(item_id)

        response = RequestSender.send_delete_catalog_item_by_id(params)
        self.assertEqual(response.status_code, 404)
