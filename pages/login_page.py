from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#Username")
        self.password_input = page.locator("#Password")
        self.login_button = page.locator(".btn.btn-primary")
        self.error_message = page.locator(".danger.validation-summary-errors li")

    def set_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.set_credentials(username, password)
        self.click_login()

    def verify_error_message(self, message):
        error_message = self.page.locator(".danger.validation-summary-errors li", has_text=message)
        expect(error_message).to_have_text(message)
