import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_valid_login(browser):
    home_page = HomePage(browser)
    login_page = LoginPage(browser)

    home_page.open()
    home_page.click_sign_in()
    login_page.login("alice", "Pass123$")
    home_page.verify_login("alice")