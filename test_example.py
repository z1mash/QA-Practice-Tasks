from playwright.sync_api import sync_playwright, expect

class HomePage:
    def __init__(self, page):
        self.page = page
        self.sign_in_button = page.locator("//*[@aria-label='Sign in']")

    def open(self):
        self.page.goto("https://localhost:7298/")

    def click_sign_in(self):
        self.sign_in_button.click()

    def verify_login(self, username):
        expect(self.page.get_by_text(username)).to_be_visible()

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#Username")
        self.password_input = page.locator("#Password")
        self.login_button = page.locator(".btn.btn-primary")

    def set_credentials(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def login(self, username, password):
        self.set_credentials(username, password)
        self.click_login()

class LoginTest:
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.home_page = HomePage(self.page)
        self.login_page = LoginPage(self.page)

    def test_login(self):
        self.home_page.open()
        self.home_page.click_sign_in()
        self.login_page.login("alice", "Pass123$")
        self.home_page.verify_login("alice")
        self.browser.close()

with sync_playwright() as playwright:
    test = LoginTest(playwright)
    test.test_login()