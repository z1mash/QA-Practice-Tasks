from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestAddToCartAndCheckout:
    def test_add_to_cart_and_checkout(self, request):
        browser = request.getfixturevalue('browser')
        
        home_page = HomePage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)
        
        home_page.open("https://localhost:7298/")

        home_page.click_product("Alpine Peak Down Jacket")
        home_page.add_to_cart()
        home_page.go_to_cart()
        cart_page.checkout()
        checkout_page.verify_order_placed()