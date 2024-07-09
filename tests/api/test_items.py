import allure
import pytest
from api.request_sender import RequestSender
from api.request_params_creator import RequestParamsCreator


@allure.feature('Catalog Items Pagination and Validation')
@pytest.mark.get_items
class TestAPI:
    @classmethod
    def setup_class(cls):
        cls.params_creator = RequestParamsCreator(api_version=1.0)

    @pytest.mark.parametrize("pageIndex, pageSize", [
        (-1, 10),
        (0, -1),
    ])
    @allure.story('Negative Pagination Parameters')
    @allure.title('Test negative pagination parameters: pageIndex={pageIndex}, pageSize={pageSize}')
    @allure.description('This test verifies the response when negative pagination parameters are provided.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_negative_pagination_parameters(self, pageIndex, pageSize):
        params = self.params_creator.get_catalog_items_params(pageIndex=pageIndex, pageSize=pageSize)
        response = RequestSender.send_catalog_items(params)
        assert response.status_code == 400

    @allure.story('Single Item Pages Are Different')
    @allure.title('Test single item pages are different')
    @allure.description('This test verifies that single item pages contain different items.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_single_item_pages_are_different(self):
        params_first = self.params_creator.get_catalog_items_params(pageIndex=0, pageSize=1)
        response_first = RequestSender.send_catalog_items(params_first)
        assert response_first.status_code == 200
        assert len(response_first.json()['data']) == 1
        first_item = response_first.json()['data'][0]

        params_second = self.params_creator.get_catalog_items_params(pageIndex=1, pageSize=1)
        response_second = RequestSender.send_catalog_items(params_second)
        assert response_second.status_code == 200
        assert len(response_second.json()['data']) == 1
        second_item = response_second.json()['data'][0]

        assert first_item != second_item

    @allure.story('Page Size 20')
    @allure.title('Test page size 20')
    @allure.description('This test verifies the response when a page size of 20 is provided.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_page_size_20(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=0, pageSize=20)
        response = RequestSender.send_catalog_items(params)
        assert response.status_code == 200
        assert len(response.json()['data']) == 20

    @allure.story('Name Not None')
    @allure.title('Test name not none')
    @allure.description('This test verifies that all items have a non-empty name.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_name_not_none(self):
        params = self.params_creator.get_catalog_items_params(pageIndex=0, pageSize=100)
        response = RequestSender.send_catalog_items(params)
        assert response.status_code == 200
        data = response.json()['data']
        assert len(data) == 100
        for item in data:
            assert item['name'] != ""
