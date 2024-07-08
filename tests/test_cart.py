from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestAddToCartAndCheckout:
    def test_add_to_cart_and_checkout(self, request):
        browser = request.getfixturevalue('browser')
        
        home_page = HomePage(browser)
        login_page = LoginPage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)
        
        home_page.open()
        home_page.click_sign_in()
        login_page.login("alice", "Pass123$")
        home_page.verify_login("alice")

        home_page.click_product("Alpine Peak Down Jacket")
        home_page.add_to_cart()
        home_page.go_to_cart()
        cart_page.checkout()
        checkout_page.place_order()
        checkout_page.verify_order_placed()