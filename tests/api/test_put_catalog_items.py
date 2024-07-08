import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    def test_put_catalog_item(self):
        item_data = {
            "id": 1,
            "name": "Updated Item",
            "description": "This is an updated item",
            "price": 150,
            "pictureFileName": "updated_item.jpg",
            "catalogTypeId": 1,
            "catalogType": {
                "id": 1,
                "type": "Updated Type"
            },
            "catalogBrandId": 1,
            "catalogBrand": {
                "id": 1,
                "brand": "Updated Brand"
            },
            "availableStock": 100,
            "restockThreshold": 10,
            "maxStockThreshold": 200,
            "onReorder": False
        }
        params = RequestParamsCreator.create_catalog_items_put_params(api_version=1.0, item_data=item_data)
        response = RequestSender.send_catalog_items_put(params)
        self.assertEqual(response.status_code, 201)
