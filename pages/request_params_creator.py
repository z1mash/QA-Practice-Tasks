class RequestParamsCreator:
    def __init__(self, api_version):
        self.api_version = api_version

    def get_catalog_items_params(self, pageIndex, pageSize):
        return {
            'pageIndex': pageIndex,
            'pageSize': pageSize,
            'api-version': self.api_version
        }
    
    @staticmethod
    def create_catalog_items_put_params(api_version, item_data):
        return {
            'api-version': api_version,
            'item_data': item_data
        }
    @staticmethod
    def create_catalog_items_post_params(api_version, item_data):
        return {
            'api-version': api_version,
            'item_data': item_data
        }