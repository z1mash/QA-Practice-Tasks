class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser

    def verify_order_placed(self):
        order_confirmation_message = self.browser.locator("span.status.submitted[b-tkhhwqlbn2]")
        assert order_confirmation_message.text_content() == "Submitted"