import unittest
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


@allure.feature('Catalog Types Retrieval')
@pytest.mark.get_catalog_types
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
