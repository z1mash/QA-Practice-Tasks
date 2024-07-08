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
            'pictureFileName': 'updated_item.jpg',
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










    # def test_post_and_get_item(self):
    #     unique_id = random.randint(10000, 99999)  # Генерация случайного целочисленного идентификатора
    #
    #     post_data = {
    #         "id": 21,
    #         "name": "string",
    #         "description": "string",
    #         "price": 10,
    #         "pictureFileName": "string",
    #         "catalogTypeId": 2,
    #         "catalogType": {
    #             "id": 2,
    #             "type": "string"
    #         },
    #         "catalogBrandId": 3,
    #         "catalogBrand": {
    #             "id": 4,
    #             "brand": "string"
    #         },
    #         "availableStock": 10,
    #         "restockThreshold": 0,
    #         "maxStockThreshold": 10,
    #         "onReorder": True
    #     }
    #     post_params = self.params_creator.create_catalog_items_post_params(api_version='1.0', item_data=post_data)
    #
    #     post_response = RequestSender.send_catalog_items_post(post_params)
    #     self.assertEqual(post_response.status_code, 201)
    #
    #     get_params = self.params_creator.create_catalog_item_by_id_params(unique_id)
    #     get_response = RequestSender.send_catalog_item_by_id_get(get_params)
    #     self.assertEqual(get_response.status_code, 200)
    #
    #     # Check if the response content type is JSON
    #     if 'application/json' in get_response.headers.get('Content-Type', ''):
    #         try:
    #             get_data = get_response.json()
    #         except ValueError as e:
    #             print(f"Error decoding JSON: {e}")
    #             print(f"Response content: {get_response.content}")
    #             raise
    #
    #         self.assertEqual(get_data['id'], post_data['id'])
    #         self.assertEqual(get_data['name'], post_data['name'])
    #         self.assertEqual(get_data['description'], post_data['description'])
    #         self.assertEqual(get_data['price'], post_data['price'])
    #         self.assertEqual(get_data['pictureFileName'], post_data['pictureFileName'])
    #         self.assertEqual(get_data['catalogTypeId'], post_data['catalogTypeId'])
    #         self.assertEqual(get_data['catalogBrandId'], post_data['catalogBrandId'])
    #         self.assertEqual(get_data['availableStock'], post_data['availableStock'])
    #         self.assertEqual(get_data['restockThreshold'], post_data['restockThreshold'])
    #         self.assertEqual(get_data['maxStockThreshold'], post_data['maxStockThreshold'])
    #         self.assertEqual(get_data['onReorder'], post_data['onReorder'])
    #     else:
    #         print("Response is not JSON. Content-Type:", get_response.headers.get('Content-Type'))
    #         print("Response content:", get_response.content)
    #         self.fail("Response is not JSON")

