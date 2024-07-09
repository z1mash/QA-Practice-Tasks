import allure

class RequestParamsCreator:
    def __init__(self, api_version):
        self.api_version = api_version

    @allure.step('Get catalog items params')
    def get_catalog_items_params(self, pageIndex, pageSize):
        return {
            'pageIndex': pageIndex,
            'pageSize': pageSize,
            'api-version': self.api_version
        }

    @allure.step('Create catalog items put params')
    def create_catalog_items_put_params(self, item_data):
        return {
            'api-version': self.api_version,
            'item_data': item_data
        }

    @allure.step('Create catalog items post params')
    def create_catalog_items_post_params(self, item_data):
        return {
            'api-version': self.api_version,
            'item_data': item_data
        }

    @allure.step('Create catalog items by params')
    def create_catalog_items_by_params(self, ids):
        return {
            'api-version': self.api_version,
            'ids': ids
        }

    @allure.step('Create catalog item by id params')
    def create_catalog_item_by_id_params(self, id):
        return {
            'api-version': self.api_version,
            'id': id
        }

    @allure.step('Create delete catalog item by id params')
    def create_delete_catalog_item_by_id_params(self, id):
        return {
            'id': id,
            'api-version': self.api_version
        }

    @allure.step('Create catalog items by name params')
    def create_catalog_items_by_name_params(self, pageSize, pageIndex, name):
        return {
            'pageSize': pageSize,
            'pageIndex': pageIndex,
            'name': name,
            'api-version': self.api_version
        }

    @allure.step('Create catalog item pic params')
    def create_catalog_item_pic_params(self, catalogItemId):
        return {
            'id': catalogItemId,
            'api-version': self.api_version
        }

    @allure.step('Create catalog items with semantic relevance params')
    def create_catalog_items_with_semantic_relevance_params(self, pageIndex, pageSize, text):
        return {
            'pageIndex': pageIndex,
            'pageSize': pageSize,
            'text': text,
            'api-version': self.api_version
        }

    @allure.step('Create catalog items by type and brand params')
    def create_catalog_items_by_type_and_brand_params(self, pageIndex, pageSize, typeId, brandId):
        return {
            'pageIndex': pageIndex,
            'pageSize': pageSize,
            'typeId': typeId,
            'brandId': brandId,
            'api-version': self.api_version
        }

    @allure.step('Create catalog items by brand params')
    def create_catalog_items_by_brand_params(self, pageSize, pageIndex, brandId):
        return {
            'pageSize': pageSize,
            'pageIndex': pageIndex,
            'brandId': brandId,
            'api-version': self.api_version
        }

    @allure.step('Create catalog types params')
    def create_catalog_types_params(self):
        return {
            'api-version': self.api_version
        }

    @allure.step('Create catalog brands params')
    def create_catalog_brands_params(self):
        return {
            'api-version': self.api_version
        }