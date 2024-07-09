import unittest
import random
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator
from api.item_factory import ItemFactory


@allure.feature('Catalog Item Management')
@pytest.mark.put_catalog_items
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Put Catalog Item Without Name')
    @allure.title('Test putting catalog item without name')
    @allure.description('This test verifies the response when updating a catalog item without a name.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_put_catalog_item_without_name(self):
        item_data = ItemFactory.create()
        del item_data['name']

        put_params = self.params_creator.create_catalog_items_put_params(item_data=item_data)
        response = RequestSender.send_catalog_items_put(put_params)

        self.assertEqual(response.status_code, 404)

    @allure.story('Post, Put and Get Item')
    @allure.title('Test posting, putting and getting a catalog item')
    @allure.description('This test verifies the creation, update, and retrieval of a catalog item.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_post_put_and_get_item(self):
        unique_id = random.randint(10000, 99999)

        post_data = ItemFactory.create()
        post_params = self.params_creator.create_catalog_items_post_params(item_data=post_data)

        post_response = RequestSender.send_catalog_items_post(post_params)
        self.assertEqual(post_response.status_code, 201, f"Unexpected status code: {post_response.status_code}")
        
        id = post_data['id']
        put_data = ItemFactory.create_with_id(id)
        put_params = self.params_creator.create_catalog_items_put_params(item_data=put_data)

        put_response = RequestSender.send_catalog_items_put(put_params)
        self.assertEqual(put_response.status_code, 201, f"Unexpected status code: {put_response.status_code}")
        

        get_params = self.params_creator.create_catalog_item_by_id_params(id=put_data['id'])
        get_response = RequestSender.send_catalog_item_by_id_get(get_params)
        self.assertEqual(get_response.status_code, 200, f"Unexpected status code: {get_response.status_code}")

        get_data = get_response.json()
        self.assertEqual(get_data['id'], put_data['id'])
        self.assertEqual(get_data['name'], put_data['name'])
        self.assertEqual(get_data['description'], put_data['description'])
        self.assertEqual(get_data['price'], put_data['price'])
        self.assertEqual(get_data['pictureFileName'], put_data['pictureFileName'])
        self.assertEqual(get_data['catalogTypeId'], put_data['catalogTypeId'])
        self.assertEqual(get_data['catalogBrandId'], put_data['catalogBrandId'])
        self.assertEqual(get_data['availableStock'], put_data['availableStock'])
        self.assertEqual(get_data['restockThreshold'], put_data['restockThreshold'])
        self.assertEqual(get_data['maxStockThreshold'], put_data['maxStockThreshold'])
        self.assertEqual(get_data['onReorder'], put_data['onReorder'])
