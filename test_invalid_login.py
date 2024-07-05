import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_message", [
    ("", "Pass123$", "The Username field is required."),
    ("alice", "", "The Password field is required."),
    ("invalid_user", "invalid_password", "Invalid username or password")
])
def test_invalid_login(browser, username, password, expected_message):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)

    home_page.open()
    home_page.click_sign_in()
    login_page.login(username, password)
    login_page.verify_error_message(expected_message)