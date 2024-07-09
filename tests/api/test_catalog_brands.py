import unittest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator
import pytest
import allure


@allure.feature('Catalog API')
@pytest.mark.catalog_brands
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Get Catalog Types')
    @allure.title('Test getting catalog types')
    @allure.description('This test verifies the retrieval of catalog types.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_catalog_types(self):
        params = self.params_creator.create_catalog_types_params()

        response = RequestSender.send_catalog_types_get(params)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsInstance(response_data, list, "Response data is not a list")
        self.assertGreater(len(response_data), 0, "Response data is empty")

        expected_types = {"Bags", "Climbing", "Cycling", "Footwear", "Jackets", "Navigation", "Ski/boarding",
                          "Trekking"}
        actual_types = {item['type'] for item in response_data}

        self.assertTrue(expected_types.issubset(actual_types),
                        f"Expected types not found in response: {expected_types - actual_types}")

    @allure.story('Get Catalog Brands')
    @allure.title('Test getting catalog brands')
    @allure.description('This test verifies the retrieval of catalog brands.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_catalog_brands(self):
        params = self.params_creator.create_catalog_brands_params()

        response = RequestSender.send_catalog_brands_get(params)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIsInstance(response_data, list, "Response data is not a list")
        self.assertGreater(len(response_data), 0, "Response data is empty")

        expected_brands = {"AirStrider", "B&R", "Daybird", "Gravitator", "Green Equipment", "Grolltex", "Legend",
                           "Quester", "Raptor Elite", "Solstix", "WildRunner", "XE", "Zephyr"}
        actual_brands = set()

        for item in response_data:
            if 'brand' in item:
                actual_brands.add(item['brand'])
            else:
                print(f"Item missing 'brand' key: {item}")

        self.assertTrue(expected_brands.issubset(actual_brands),
                        f"Expected brands not found in response: {expected_brands - actual_brands}")
