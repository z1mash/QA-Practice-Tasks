import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

class TestLogin:
    @pytest.mark.parametrize("username, password, expected_message", [
        ("", "Pass123$", "The Username field is required."),
        ("alice", "", "The Password field is required."),
        ("invalid_user", "invalid_password", "Invalid username or password"),
        ("", "", "The Username field is required.")
    ])
    def test_invalid_login(self, request, username, password, expected_message):
        browser = request.getfixturevalue('browser')
        home_page = HomePage(browser)
        login_page = LoginPage(browser)

        home_page.open()
        home_page.click_sign_in()
        login_page.login(username, password)
        login_page.verify_error_message(expected_message)

    def test_valid_login(self, request):
        browser = request.getfixturevalue('browser')
        home_page = HomePage(browser)
        login_page = LoginPage(browser)

        home_page.open()
        home_page.click_sign_in()
        login_page.login("alice", "Pass123$")
        home_page.verify_login("alice")