import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_item_by_id(self):
        item_id = 1
        params = self.params_creator.create_catalog_item_by_id_params(item_id)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertEqual(response_data['id'], item_id, f"Unexpected item ID: {response_data['id']}")

    def test_get_nonexistent_catalog_item_by_id(self):
        nonexistent_item_id = 999999
        params = self.params_creator.create_catalog_item_by_id_params(nonexistent_item_id)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 404, f"Unexpected status code: {response.status_code}")

    def test_get_catalog_item_by_invalid_id(self):
        invalid_item_id = -1
        params = self.params_creator.create_catalog_item_by_id_params(invalid_item_id)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 400, f"Unexpected status code: {response.status_code}")
