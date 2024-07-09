import allure
from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.locator("//*[@aria-label='Sign in']")

    @allure.step('Open home page')
    def open(self):
        self.page.goto("https://localhost:7298/")

    @allure.step('Click sign in button')
    def click_sign_in(self):
        self.sign_in_button.click()

    @allure.step('Verify login for user {username}')
    def verify_login(self, username):
        expect(self.page.get_by_text(username)).to_be_visible(timeout=10000)

    @allure.step('Add product to cart')
    def add_to_cart(self):
        add_to_cart_button = self.page.locator("button[type='submit'][title='Add to basket'][b-day7kai9gc]")
        add_to_cart_button.click()

    @allure.step('Go to cart page')
    def go_to_cart(self):
        cart_link = self.page.locator("a[href='cart'][b-day7kai9gc]")
        cart_link.click()

    @allure.step('Click on product {product_name}')
    def click_product(self, product_name):
        product_locator = self.page.locator(f"//*[contains(text(), '{product_name}')]")
        product_locator.click()
