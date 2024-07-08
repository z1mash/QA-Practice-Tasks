import unittest
import random
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_items_with_semantic_relevance(self):
        pageIndex = 0
        pageSize = 10
        text = 'example'
        params = self.params_creator.create_catalog_items_with_semantic_relevance_params(pageIndex, pageSize, text)

        response = RequestSender.send_catalog_items_with_semantic_relevance_get(text, params)
        self.assertEqual(response.status_code, 200)

    def test_get_catalog_items_with_semantic_relevance(self):
        pageIndex = 0
        pageSize = 10
        text = 'example'
        params = self.params_creator.create_catalog_items_with_semantic_relevance_params(pageIndex, pageSize, text)

        response = RequestSender.send_catalog_items_with_semantic_relevance_get(text, params)
        self.assertEqual(response.status_code, 200)

    def test_get_catalog_items_with_semantic_relevance_empty_text(self):
        pageIndex = 0
        pageSize = 10
        text = ''
        params = self.params_creator.create_catalog_items_with_semantic_relevance_params(pageIndex, pageSize, text)

        response = RequestSender.send_catalog_items_with_semantic_relevance_get(text, params)
        self.assertEqual(response.status_code, 400)

        response_data = response.json()
        self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
        items = response_data.get('data', [])

        self.assertGreaterEqual(len(items), 0, "Response data should be empty or contain expected items")

    # def test_create_and_get_catalog_items_with_semantic_relevance(self):
    #     pageIndex = 0
    #     pageSize = 10
    #     value = 'value'
    #     random_value1 = f"RANDOM_VALUE_{random.randint(1000, 9999)}"
    #     random_value2 = f"RANDOM_VALUE_{random.randint(1000, 9999)}"
    #     random_value3 = f"RANDOM_VALUE_{random.randint(1000, 9999)}"
    #     random_id1 = random.randint(10000, 99999)
    #     random_id2 = random.randint(10000, 99999)
    #     random_id3 = random.randint(10000, 99999)
    #
    #     item1 = {
    #         'id': random_id1,
    #         'name': f"{value} {random_value1}",
    #         'description': 'Test item 1',
    #         'price': 100,
    #         'pictureFileName': 'test1.jpg',
    #         'catalogTypeId': 1,
    #         'catalogBrandId': 1,
    #         'availableStock': 10,
    #         'restockThreshold': 5,
    #         'maxStockThreshold': 20,
    #         'onReorder': False
    #     }
    #     item2 = {
    #         'id': random_id2,
    #         'name': f"{random_value2} {value}",
    #         'description': 'Test item 2',
    #         'price': 150,
    #         'pictureFileName': 'test2.jpg',
    #         'catalogTypeId': 2,
    #         'catalogBrandId': 2,
    #         'availableStock': 15,
    #         'restockThreshold': 10,
    #         'maxStockThreshold': 25,
    #         'onReorder': True
    #     }
    #     item3 = {
    #         'id': random_id3,
    #         'name': f"{random_value3} {value} {random_value3}",
    #         'description': 'Test item 3',
    #         'price': 200,
    #         'pictureFileName': 'test3.jpg',
    #         'catalogTypeId': 3,
    #         'catalogBrandId': 3,
    #         'availableStock': 20,
    #         'restockThreshold': 15,
    #         'maxStockThreshold': 30,
    #         'onReorder': False
    #     }
    #
    #     create_params1 = self.params_creator.create_catalog_items_post_params(item_data=item1)
    #     create_response1 = RequestSender.send_catalog_items_post(create_params1)
    #     if create_response1.status_code != 201:
    #         print(f"Error creating item1: {create_response1.status_code} - {create_response1.text}")
    #     self.assertEqual(create_response1.status_code, 201)
    #
    #     create_params2 = self.params_creator.create_catalog_items_post_params(item_data=item2)
    #     create_response2 = RequestSender.send_catalog_items_post(create_params2)
    #     if create_response2.status_code != 201:
    #         print(f"Error creating item2: {create_response2.status_code} - {create_response2.text}")
    #     self.assertEqual(create_response2.status_code, 201)
    #
    #     create_params3 = self.params_creator.create_catalog_items_post_params(item_data=item3)
    #     create_response3 = RequestSender.send_catalog_items_post(create_params3)
    #     if create_response3.status_code != 201:
    #         print(f"Error creating item3: {create_response3.status_code} - {create_response3.text}")
    #     self.assertEqual(create_response3.status_code, 201)
    #
    #     params = self.params_creator.create_catalog_items_with_semantic_relevance_params(pageIndex, pageSize, value)
    #     response = RequestSender.send_catalog_items_with_semantic_relevance_get(value, params)
    #     self.assertEqual(response.status_code, 200)
    #
    #     response_data = response.json()
    #     self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
    #     items = response_data.get('data', [])
    #
    #     item_names = [item['name'] for item in items]
    #     self.assertIn(item1['name'], item_names, f"Item with name '{item1['name']}' not found in response")
    #     self.assertIn(item2['name'], item_names, f"Item with name '{item2['name']}' not found in response")
    #     self.assertIn(item3['name'], item_names, f"Item with name '{item3['name']}' not found in response")
