import unittest
import random
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_items_by_name(self):
        pageSize = 10
        pageIndex = 123
        name = 'Item'
        params = self.params_creator.create_catalog_items_by_name_params(pageSize, pageIndex, name)

        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
        items = response_data.get('data', [])
        self.assertIsInstance(items, list, "Items data is not a list")

        for item in items:
            self.assertIsInstance(item, dict, f"Item is not a dictionary: {item}")
            self.assertIn(name.lower(), item['name'].lower(), f"Item name '{item['name']}' does not contain '{name}'")

    def test_get_catalog_items_by_name_page_size(self):
        pageSize = 10
        pageIndex = 12
        name = 'Item'
        params = self.params_creator.create_catalog_items_by_name_params(pageSize, pageIndex, name)

        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
        items = response_data.get('data', [])
        self.assertEqual(len(items), pageSize, f"Unexpected number of items: {len(items)}")

    def test_get_catalog_items_by_name_page_index(self):
        pageSize = 10
        pageIndex = 12
        name = 'Item'
        params = self.params_creator.create_catalog_items_by_name_params(pageSize, pageIndex, name)

        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

    def test_create_and_get_catalog_items_with_same_name(self):
        unique_name = f"TestItem_{random.randint(1000, 9999)}"
        unique_id1 = random.randint(10000, 99999)
        unique_id2 = random.randint(300, 1000)

        item_data1 = {
            'id': unique_id1,
            'name': unique_name,
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
        create_params1 = self.params_creator.create_catalog_items_post_params(item_data=item_data1)
        create_response1 = RequestSender.send_catalog_items_post(create_params1)
        self.assertEqual(create_response1.status_code, 201)

        item_data2 = {
            'id': unique_id2,
            'name': unique_name,
            'description': 'This is another test item',
            'price': 150,
            'pictureFileName': 'test2.jpg',
            'catalogTypeId': 2,
            'catalogBrandId': 2,
            'availableStock': 15,
            'restockThreshold': 10,
            'maxStockThreshold': 25,
            'onReorder': True
        }
        create_params2 = self.params_creator.create_catalog_items_post_params(item_data=item_data2)
        create_response2 = RequestSender.send_catalog_items_post(create_params2)
        self.assertEqual(create_response2.status_code, 201)

        pageSize = 10
        pageIndex = 0
        params = self.params_creator.create_catalog_items_by_name_params(pageSize, pageIndex, unique_name)
        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertGreaterEqual(len(response_data), 2, f"Expected at least 2 items, but found {len(response_data)}")


