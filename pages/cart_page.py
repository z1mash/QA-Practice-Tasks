import allure

class CartPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Proceed to checkout')
    def checkout(self):
        checkout_button = self.browser.locator("a[href='checkout'].button.button-primary[b-hye5arey4f]")
        checkout_button.click()