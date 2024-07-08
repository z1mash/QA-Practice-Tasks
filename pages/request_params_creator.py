class RequestParamsCreator:
    def __init__(self, api_version):
        self.api_version = api_version

    def get_catalog_items_params(self, pageIndex, pageSize):
        return {
            'pageIndex': pageIndex,
            'pageSize': pageSize,
            'api-version': self.api_version
        }