import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    # не робит
    # def test_create_and_delete_catalog_item(self):
    #     item_data = {
    #         'name': 'Test Item',
    #         'description': 'This is a test item',
    #         'price': 100,
    #         'pictureFileName': 'test.jpg',
    #         'catalogTypeId': 1,
    #         'catalogBrandId': 1,
    #         'availableStock': 10,
    #         'restockThreshold': 5,
    #         'maxStockThreshold': 20,
    #         'onReorder': False
    #     }
    #     create_params = self.params_creator.create_catalog_items_post_params(item_data)
    #     create_response = RequestSender.send_catalog_items(create_params)
    #     self.assertEqual(create_response.status_code, 201)

    #     # Получение ID созданного элемента
    #     created_item = create_response.json()
    #     item_id = created_item['id']

    #     # Удаление элемента
    #     delete_params = self.params_creator.create_delete_catalog_item_by_id_params(item_id)
    #     delete_response = RequestSender.send_delete_catalog_item_by_id(delete_params)
    #     self.assertEqual(delete_response.status_code, 204)

    # робит, но не так как надо
    def test_delete_non_existing_catalog_item(self):
        item_id = 9999  # Замените на несуществующий ID
        params = self.params_creator.create_delete_catalog_item_by_id_params(item_id)

        response = RequestSender.send_delete_catalog_item_by_id(params)
        self.assertEqual(response.status_code, 404)
