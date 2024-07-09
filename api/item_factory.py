import random
import allure


class ItemFactory:
    @staticmethod
    @allure.step("Create a new item with random attributes")
    def create():
        id = random.randint(10000, 99999)
        value = f"RANDOM_{random.randint(1000, 9999)}"
        price = random.randint(20, 300)
        description = f"This is a test item_{random.randint(0, 10)}"

        return {
            'id': id,
            'name': f"{value}",
            'description': description,
            'price': price,
            'pictureFileName': '99.webp',
            'catalogTypeId': 1,
            'catalogBrandId': 1,
            'availableStock': 10,
            'restockThreshold': 5,
            'maxStockThreshold': 20,
            'onReorder': False
        }

    @staticmethod
    @allure.step("Create a new item with a specific name")
    def create_with_name(name):
        item = ItemFactory.create()
        item['name'] = name
        return item

    @staticmethod
    @allure.step("Create a new item with a specific ID")
    def create_with_id(id):
        item = ItemFactory.create()
        item['id'] = id
        return item
