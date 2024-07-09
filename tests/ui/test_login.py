import sys
import os
import allure

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.feature('Login Functionality')
@pytest.mark.ui_login
class TestLogin:
    @pytest.mark.parametrize("username, password, expected_message", [
        ("", "Pass123$", "The Username field is required."),
        ("alice", "", "The Password field is required."),
        ("invalid_user", "invalid_password", "Invalid username or password"),
        ("", "", "The Username field is required.")
    ])
    @allure.story('Invalid Login Scenarios')
    @allure.title('Test invalid login with username: {username} and password: {password}')
    @allure.description('This test verifies the error message for invalid login attempts.')
    @allure.severity(allure.severity_level.NORMAL)
    def test_invalid_login(self, browser, username, password, expected_message):
        home_page = HomePage(browser)
        login_page = LoginPage(browser)

        with allure.step('Open home page'):
            home_page.open()

        with allure.step('Click sign in button'):
            home_page.click_sign_in()

        with allure.step('Login with username: {username} and password: {password}'.format(username=username,
                                                                                           password=password)):
            login_page.login(username, password)

        with allure.step('Verify error message: {expected_message}'.format(expected_message=expected_message)):
            login_page.verify_error_message(expected_message)

    @allure.story('Valid Login Scenario')
    @allure.title('Test valid login with username: alice and password: Pass123$')
    @allure.description('This test verifies the successful login process.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_valid_login(self, browser):
        home_page = HomePage(browser)
        login_page = LoginPage(browser)

        with allure.step('Open home page'):
            home_page.open()

        with allure.step('Click sign in button'):
            home_page.click_sign_in()

        with allure.step('Login with username: alice and password: Pass123$'):
            login_page.login("alice", "Pass123$")

        with allure.step('Verify login for user: alice'):
            home_page.verify_login("alice")
