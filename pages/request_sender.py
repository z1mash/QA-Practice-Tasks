import requests
from pages.constants import BASE_URL, CATALOG_ITEMS_ENDPOINT 

class RequestSender:
    @staticmethod
    def send_catalog_items(params):
        url = f"{BASE_URL}{CATALOG_ITEMS_ENDPOINT}"
        response = requests.get(url, params=params)
        return response
    