import unittest
import random
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator
from api.item_factory import ItemFactory


@allure.feature('Catalog Items by Name Retrieval')
@pytest.mark.get_catalog_items_by_name
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Get Catalog Items by Name')
    @allure.title('Test getting catalog items by name')
    @allure.description('This test verifies the retrieval of catalog items by a specific name.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
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

    @allure.story('Get Catalog Items by Name with Page Size')
    @allure.title('Test getting catalog items by name with specific page size')
    @allure.description(
        'This test verifies the retrieval of catalog items by a specific name with a specific page size.')
    @allure.severity(allure.severity_level.NORMAL)
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

    @allure.story('Get Catalog Items by Name with Page Index')
    @allure.title('Test getting catalog items by name with specific page index')
    @allure.description(
        'This test verifies the retrieval of catalog items by a specific name with a specific page index.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_catalog_items_by_name_page_index(self):
        pageSize = 10
        pageIndex = 12
        name = 'Item'
        params = self.params_creator.create_catalog_items_by_name_params(pageSize, pageIndex, name)

        response = RequestSender.send_catalog_items(params)
        self.assertEqual(response.status_code, 200)

    @allure.story('Create and Get Catalog Items with Same Name')
    @allure.title('Test creating and getting catalog items with the same name')
    @allure.description('This test verifies the creation and retrieval of catalog items with the same name.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_and_get_catalog_items_with_same_name(self):
        unique_name = f"TestItem_{random.randint(1000, 9999)}"

        item_data1 = ItemFactory.create()
        create_params1 = self.params_creator.create_catalog_items_post_params(item_data=item_data1)
        create_response1 = RequestSender.send_catalog_items_post(create_params1)
        self.assertEqual(create_response1.status_code, 201)

        item_data2 = ItemFactory.create()
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
