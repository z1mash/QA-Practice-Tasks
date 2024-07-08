import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version=1.0)

    def test_get_catalog_items_by(self):
        ids = [1, 2, 3]
        params = self.params_creator.create_catalog_items_by_params(ids)

        response = RequestSender.send_catalog_items_by_get(params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        response_ids = [item['id'] for item in response_data]

        for id in ids:
            self.assertIn(id, response_ids, f"ID {id} not found in response")

        for id in response_ids:
            self.assertIn(id, ids, f"Unexpected ID {id} found in response")

    def test_get_nonexistent_catalog_items_by(self):
        nonexistent_ids = [999999, 888888]
        params = self.params_creator.create_catalog_items_by_params(nonexistent_ids)

        response = RequestSender.send_catalog_items_by_get(params)
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")

    def test_get_catalog_items_by_invalid_id(self):
        invalid_ids = [-1, -2]
        params = self.params_creator.create_catalog_items_by_params(invalid_ids)

        response = RequestSender.send_catalog_items_by_get(params)
        self.assertEqual(response.status_code, 200, f"Unexpected status code: {response.status_code}")
