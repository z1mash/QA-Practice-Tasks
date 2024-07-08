import unittest
import random
from pages.request_sender import RequestSender
from pages.request_params_creator import RequestParamsCreator

class TestAPI(unittest.TestCase):
    def test_post_catalog_item(self):
        item_data = {
            "id": random.randint(50000, 100000),
            "name": "New Item",
            "description": "This is a new item",
            "price": 100,
            "pictureFileName": "new_item.jpg",
            "catalogTypeId": 1,
            "catalogType": {
                "id": random.randint(1, 100),
                "type": "New Type"
            },
            "catalogBrandId": 1,
            "catalogBrand": {
                "id": random.randint(1, 100),
                "brand": "New Brand"
            },
            "availableStock": 50,
            "restockThreshold": 5,
            "maxStockThreshold": 100,
            "onReorder": False
        }
        params = RequestParamsCreator.create_catalog_items_post_params(api_version=1.0, item_data=item_data)
        response = RequestSender.send_catalog_items_post(params)
        self.assertEqual(response.status_code, 201)
