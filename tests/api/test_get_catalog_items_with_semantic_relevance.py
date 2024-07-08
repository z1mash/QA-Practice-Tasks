import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    def test_get_catalog_items_with_semantic_relevance(self):
        pageIndex = 0
        pageSize = 10
        text = 'example'  # Замените на нужный текст
        params = self.params_creator.create_catalog_items_with_semantic_relevance_params(pageIndex, pageSize, text)

        response = RequestSender.send_catalog_items_with_semantic_relevance_get(text, params)
        self.assertEqual(response.status_code, 200)
