import requests
from api.constants import *


class RequestSender:
    @staticmethod
    def send_catalog_items(params):
        url = f"{BASE_URL}{CATALOG_ITEMS_ENDPOINT}"
        response = requests.get(url, params=params)
        return response

    @staticmethod
    def send_catalog_items_put(params):
        url = f"{BASE_URL}{CATALOG_ITEMS_ENDPOINT}?api-version={params['api-version']}"
        response = requests.put(url, json=params['item_data'])
        return response

    @staticmethod
    def send_catalog_items_post(params):
        url = f"{BASE_URL}{CATALOG_ITEMS_ENDPOINT}?api-version={params['api-version']}"
        response = requests.post(url, json=params['item_data'])
        return response

    @staticmethod
    def send_catalog_items_by_get(params):
        ids_params = '&'.join([f'ids={id}' for id in params['ids']])
        url = f"{BASE_URL}{CATALOG_ITEMS_BY_ENDPOINT}?{ids_params}&api-version={params['api-version']}"
        return requests.get(url)

    @staticmethod
    def send_catalog_item_by_id_get(params):
        url = f"{BASE_URL}{CATALOG_ITEM_BY_ID_ENDPOINT.format(id=params['id'])}?api-version={params['api-version']}"
        return requests.get(url)

    @staticmethod
    def send_delete_catalog_item_by_id(params):
        url = f"{BASE_URL}{CATALOG_ITEM_BY_ID_ENDPOINT.format(id=params['id'])}?api-version={params['api-version']}"
        return requests.delete(url)

    @staticmethod
    def send_catalog_items_by_name_get(name, params):
        url = f"{BASE_URL}{CATALOG_ITEMS_BY_NAME_ENDPOINT.format(name=name)}"
        query_params = {
            'pageSize': params['pageSize'],
            'pageIndex': params['pageIndex'],
            'api-version': params['api-version']
        }
        return requests.get(url, params=query_params)

    @staticmethod
    def send_catalog_item_by_pic_get(params):
        url = f"{BASE_URL}{CATALOG_ITEM_PIC_ENDPOINT.format(catalogItemId=params['id'])}?api-version={params['api-version']}"
        return requests.get(url)

    @staticmethod
    def send_catalog_items_with_semantic_relevance_get(text, params):
        url = f"{BASE_URL}{CATALOG_ITEMS_WITH_SEMANTIC_RELEVANCE_ENDPOINT.format(text=text)}"
        query_params = {
            'pageIndex': params['pageIndex'],
            'pageSize': params['pageSize'],
            'api-version': params['api-version']
        }
        return requests.get(url, params=query_params)

    @staticmethod
    def send_catalog_items_by_type_and_brand_get(typeId, brandId, params):
        url = f"{BASE_URL}{CATALOG_ITEMS_BY_TYPE_AND_BRAND_ENDPOINT.format(typeId=typeId, brandId=brandId)}"
        query_params = {
            'pageIndex': params['pageIndex'],
            'pageSize': params['pageSize'],
            'api-version': params['api-version']
        }
        return requests.get(url, params=query_params)

    @staticmethod
    def send_catalog_items_by_brand_get(brandId, params):
        url = f"{BASE_URL}{CATALOG_ITEMS_BY_BRAND_ENDPOINT.format(brandId=brandId)}"
        query_params = {
            'pageSize': params['pageSize'],
            'pageIndex': params['pageIndex'],
            'api-version': params['api-version']
        }
        return requests.get(url, params=query_params)

    @staticmethod
    def send_catalog_types_get(params):
        url = f"{BASE_URL}{CATALOG_TYPES_ENDPOINT}"
        query_params = {
            'api-version': params['api-version']
        }
        return requests.get(url, params=query_params)

    @staticmethod
    def send_catalog_brands_get(params):
        url = f"{BASE_URL}{CATALOG_BRANDS_ENDPOINT}"
        query_params = {
            'api-version': params['api-version']
        }
        return requests.get(url, params=query_params)
