import allure


class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step('Place order')
    def place_order(self):
        place_order_button = self.browser.locator("button.button.button-primary[type='submit'][b-ekak8lzpb0]")
        place_order_button.click()

    @allure.step('Verify order placed')
    def verify_order_placed(self):
        order_confirmation_message = self.browser.locator("span.status.submitted[b-tkhhwqlbn2]")
        assert order_confirmation_message.text_content(timeout=60000) == "Submitted"
