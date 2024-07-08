import requests
from pages.constants import BASE_URL, CATALOG_ITEMS_ENDPOINT 

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