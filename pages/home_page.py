from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.sign_in_button = page.locator("//*[@aria-label='Sign in']")

    def open(self):
        self.page.goto("https://localhost:7298/")

    def click_sign_in(self):
        self.sign_in_button.click()

    def verify_login(self, username):
        expect(self.page.get_by_text(username)).to_be_visible()

    def add_to_cart(self):
        add_to_cart_button = self.browser.locator("button[type='submit'][title='Add to basket'][b-day7kai9gc]")
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_link = self.browser.locator("a[href='cart'][b-day7kai9gc]")
        cart_link.click()
