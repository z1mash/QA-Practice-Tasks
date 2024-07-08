import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version=1.0)

    def test_negative_page_size(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=0, pageSize=-1)
        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 400)

    def test_negative_page_index(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=-1, pageSize=10)
        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 400)

    def test_single_item_page_first(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=0, pageSize=1)
        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 1)
        self.__class__.first_item = response.json()['data'][0]

    def test_single_item_page_second(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=1, pageSize=1)
        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 1)
        second_item = response.json()['data'][0]
        self.assertNotEqual(self.__class__.first_item, second_item)

    def test_page_size_20(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=0, pageSize=20)
        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 20)

    def test_name_not_none(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=0, pageSize=100)
        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(len(data), 100)
        for item in data:
            self.assertNotEqual(item['name'], "")
