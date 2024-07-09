import unittest
import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


@allure.feature('Catalog Item Picture Retrieval')
@pytest.mark.get_catalog_item_pic
class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.params_creator = RequestParamsCreator(api_version='1.0')

    @allure.story('Get Catalog Item Picture by Existing ID')
    @allure.title('Test getting catalog item picture by existing ID')
    @allure.description('This test verifies the retrieval of a catalog item picture by an existing ID.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_get_catalog_item_pic_existing(self):
        catalogItemId = 1
        params = self.params_creator.create_catalog_item_pic_params(catalogItemId)

        response = RequestSender.send_catalog_item_by_id_get(params)
        self.assertEqual(response.status_code, 200)
