import allure
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature('Add to Cart and Checkout')
@pytest.mark.ui_cart
class TestAddToCartAndCheckout:
    @allure.story('Add to Cart and Complete Checkout')
    @allure.title('Test adding a product to cart and completing the checkout process')
    @allure.description('This test verifies the process of adding a product to the cart and completing the checkout.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_add_to_cart_and_checkout(self, request):
        browser = request.getfixturevalue('browser')

        home_page = HomePage(browser)
        login_page = LoginPage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)

        with allure.step('Open home page'):
            home_page.open()

        with allure.step('Click sign in button'):
            home_page.click_sign_in()

        with allure.step('Login with username "alice" and password "Pass123$"'):
            login_page.login("alice", "Pass123$")

        with allure.step('Verify login for user "alice"'):
            home_page.verify_login("alice")

        with allure.step('Click on product "Alpine Peak Down Jacket"'):
            home_page.click_product("Alpine Peak Down Jacket")

        with allure.step('Add product to cart'):
            home_page.add_to_cart()

        with allure.step('Go to cart page'):
            home_page.go_to_cart()

        with allure.step('Proceed to checkout'):
            cart_page.checkout()

        with allure.step('Place order'):
            checkout_page.place_order()

        with allure.step('Verify order placed'):
            checkout_page.verify_order_placed()
