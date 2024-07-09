import unittest
import random
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator
from api.item_factory import ItemFactory


@allure.feature('Catalog Items with Semantic Relevance Retrieval')
@pytest.mark.get_catalog_items_semantic
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Get Catalog Items with Semantic Relevance')
    @allure.title('Test getting catalog items with semantic relevance')
    @allure.description('This test verifies the retrieval of catalog items with semantic relevance.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_catalog_items_with_semantic_relevance(self):
        pageIndex = 0
        pageSize = 10
        text = 'example'
        params = self.params_creator.create_catalog_items_with_semantic_relevance_params(pageIndex, pageSize, text)

        response = RequestSender.send_catalog_items_with_semantic_relevance_get(text, params)
        self.assertEqual(response.status_code, 200)

    @allure.story('Create and Get Catalog Items with Semantic Relevance')
    @allure.title('Test creating and getting catalog items with semantic relevance')
    @allure.description('This test verifies the creation and retrieval of catalog items with semantic relevance.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_create_and_get_catalog_items_with_semantic_relevance(self):
        pageIndex = 0
        pageSize = 10
        value = f"RANDOM1_{random.randint(1000, 9999)}"
        random_value1 = f"RANDOM1_{random.randint(1000, 9999)}"
        random_value2 = f"RANDOM2_{random.randint(1000, 9999)}"
        random_value3 = f"RANDOM3_{random.randint(1000, 9999)}"

        item1 = ItemFactory.create_with_name(f"{value} {random_value1}")
        item2 = ItemFactory.create_with_name(f"{value} {random_value2}")
        item3 = ItemFactory.create_with_name(f"{value} {random_value3}")

        create_params1 = self.params_creator.create_catalog_items_post_params(item_data=item1)
        create_response1 = RequestSender.send_catalog_items_post(create_params1)
        self.assertEqual(create_response1.status_code, 201)

        create_params2 = self.params_creator.create_catalog_items_post_params(item_data=item2)
        create_response2 = RequestSender.send_catalog_items_post(create_params2)
        self.assertEqual(create_response2.status_code, 201)

        create_params3 = self.params_creator.create_catalog_items_post_params(item_data=item3)
        create_response3 = RequestSender.send_catalog_items_post(create_params3)
        self.assertEqual(create_response3.status_code, 201)

        params = self.params_creator.create_catalog_items_with_semantic_relevance_params(pageIndex, pageSize, value)
        response = RequestSender.send_catalog_items_with_semantic_relevance_get(value, params)
        self.assertEqual(response.status_code, 200)

        response_data = response.json()
        self.assertIsInstance(response_data, dict, "Response data is not a dictionary")
        items = response_data.get('data', [])

        item_names = [item['name'] for item in items]
        self.assertIn(item1['name'], item_names, f"Item with name '{item1['name']}' not found in response")
        self.assertIn(item2['name'], item_names, f"Item with name '{item2['name']}' not found in response")
        self.assertIn(item3['name'], item_names, f"Item with name '{item3['name']}' not found in response")

        print(f"Items in response: {item_names}")
        print(f"Expected items: {[item1['name'], item2['name'], item3['name']]}")
