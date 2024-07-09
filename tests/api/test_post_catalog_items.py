import unittest
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator
from api.item_factory import ItemFactory


@allure.feature('Catalog Item Management')
@pytest.mark.post_catalog_items
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Post Catalog Item Without Name')
    @allure.title('Test posting catalog item without name')
    @allure.description('This test verifies the response when posting a catalog item without a name.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_post_catalog_item_without_name(self):
        item_data = ItemFactory.create()
        del item_data['name']

        post_params = self.params_creator.create_catalog_items_post_params(item_data=item_data)
        response = RequestSender.send_catalog_items_post(post_params)

        self.assertEqual(response.status_code, 400)

    @allure.story('Post and Get Item')
    @allure.title('Test posting and getting a catalog item')
    @allure.description('This test verifies the creation and retrieval of a catalog item.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_post_and_get_item(self):
        post_data = ItemFactory.create()
        unique_id = post_data['id']
        post_params = self.params_creator.create_catalog_items_post_params(post_data)

        post_response = RequestSender.send_catalog_items_post(post_params)
        self.assertEqual(post_response.status_code, 201, f"Unexpected status code: {post_response.status_code}")

        get_params = self.params_creator.create_catalog_item_by_id_params(unique_id)
        get_response = RequestSender.send_catalog_item_by_id_get(get_params)
        self.assertEqual(get_response.status_code, 200, f"Unexpected status code: {get_response.status_code}")

        get_data = get_response.json()
        self.assertEqual(get_data['id'], post_data['id'])
        self.assertEqual(get_data['name'], post_data['name'])
        self.assertEqual(get_data['description'], post_data['description'])
        self.assertEqual(get_data['price'], post_data['price'])
        self.assertEqual(get_data['pictureFileName'], post_data['pictureFileName'])
        self.assertEqual(get_data['catalogTypeId'], post_data['catalogTypeId'])
        self.assertEqual(get_data['catalogBrandId'], post_data['catalogBrandId'])
        self.assertEqual(get_data['availableStock'], post_data['availableStock'])
        self.assertEqual(get_data['restockThreshold'], post_data['restockThreshold'])
        self.assertEqual(get_data['maxStockThreshold'], post_data['maxStockThreshold'])
        self.assertEqual(get_data['onReorder'], post_data['onReorder'])
