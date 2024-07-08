import unittest
import random
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_put_catalog_item_without_name(self):
        item_data = {
            'description': 'This is an updated item in the catalog',
            'price': 10.99,
            'pictureFileName': '99.webp',
            'catalogTypeId': 1,
            'catalogBrandId': 1,
            'availableStock': 100,
            'restockThreshold': 10,
            'maxStockThreshold': 200,
            'onReorder': False
        }

        put_params = self.params_creator.create_catalog_items_put_params(item_data=item_data)
        response = RequestSender.send_catalog_items_put(put_params)

        self.assertEqual(response.status_code, 404)

    def test_post_put_and_get_item(self):
        unique_id = random.randint(10000, 99999)

        post_data = {
            'id': unique_id,
            'name': 'Test Item',
            'description': 'This is a test item',
            'price': 100,
            'pictureFileName': '99.webp',
            'catalogTypeId': 1,
            'catalogBrandId': 1,
            'availableStock': 10,
            'restockThreshold': 5,
            'maxStockThreshold': 20,
            'onReorder': False
        }
        post_params = self.params_creator.create_catalog_items_post_params(item_data=post_data)

        post_response = RequestSender.send_catalog_items_post(post_params)
        self.assertEqual(post_response.status_code, 201, f"Unexpected status code: {post_response.status_code}")

        put_data = {
            'id': unique_id,
            'name': 'Updated Test Item',
            'description': 'This is an updated test item',
            'price': 150,
            'pictureFileName': 'updated_99.webp',
            'catalogTypeId': 2,
            'catalogBrandId': 2,
            'availableStock': 20,
            'restockThreshold': 10,
            'maxStockThreshold': 30,
            'onReorder': True
        }
        put_params = self.params_creator.create_catalog_items_put_params(item_data=put_data)

        put_response = RequestSender.send_catalog_items_put(put_params)
        self.assertEqual(put_response.status_code, 201, f"Unexpected status code: {put_response.status_code}")

        get_params = self.params_creator.create_catalog_item_by_id_params(id=unique_id)
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

