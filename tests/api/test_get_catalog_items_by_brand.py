import unittest
import random
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_items_by_brand(self):
        pageSize = 10
        pageIndex = 0
        brandId = 1
        params = self.params_creator.create_catalog_items_by_brand_params(pageSize, pageIndex, brandId)

        response = RequestSender.send_catalog_items_by_brand_get(brandId, params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
        items = response_data.get('data', [])

        for item in items:
            self.assertEqual(item['catalogBrandId'], brandId, f"Item has incorrect catalogBrandId: {item['catalogBrandId']}")

    def test_create_and_get_catalog_items_by_brand(self):
        brandId = 1
        typeId1 = 1
        typeId2 = 2
        random_id1 = random.randint(0, 100)
        random_id2 = random.randint(0, 100)

        item1 = {
            'id': random_id1,
            'name': 'Test Item 1',
            'description': 'Test item 1',
            'price': 100,
            'pictureFileName': 'test1.jpg',
            'catalogTypeId': typeId1,
            'catalogBrandId': brandId,
            'availableStock': 10,
            'restockThreshold': 5,
            'maxStockThreshold': 20,
            'onReorder': False
        }
        item2 = {
            'id': random_id2,
            'name': 'Test Item 2',
            'description': 'Test item 2',
            'price': 150,
            'pictureFileName': 'test2.jpg',
            'catalogTypeId': typeId2,
            'catalogBrandId': brandId,
            'availableStock': 15,
            'restockThreshold': 10,
            'maxStockThreshold': 25,
            'onReorder': True
        }

        create_params1 = self.params_creator.create_catalog_items_post_params(item_data=item1)
        create_response1 = RequestSender.send_catalog_items_post(create_params1)
        self.assertEqual(create_response1.status_code, 201)

        create_params2 = self.params_creator.create_catalog_items_post_params(item_data=item2)
        create_response2 = RequestSender.send_catalog_items_post(create_params2)
        self.assertEqual(create_response2.status_code, 201)

        pageSize = 10
        pageIndex = 0
        params = self.params_creator.create_catalog_items_by_brand_params(pageSize, pageIndex, brandId)
        response = RequestSender.send_catalog_items_by_brand_get(brandId, params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
        items = response_data.get('data', [])

        item_ids = [item['id'] for item in items]
        self.assertIn(item1['id'], item_ids, f"Item with id '{item1['id']}' not found in response")
        self.assertIn(item2['id'], item_ids, f"Item with id '{item2['id']}' not found in response")
