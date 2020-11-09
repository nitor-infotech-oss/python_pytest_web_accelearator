"""
@pytest.mark is used to mark a test with a particular tag
for eg: @pytest.mark.frontend, @pytest.mark.orderplace

@pytest.mark.parametrize is used to mark a test case as parameterize
and parameters can be passed in it.

@pytest.mark.run is used to mark a test in a particular order
for eg: @pytest.mark.run(order=1) to run the test case first

This test file consist of test cases related to placing order.
"""
import pytest
from pytest_practical.tests.pages.fashion_site_cart_page import fashion_site_cart_page
from pytest_practical.tests.pages.fashion_site_home_page import fashion_site_home_page
from pytest_practical.tests.pages.fashion_site_checkout_page import fashion_site_checkout_page
from pytest_practical.tests.pages.fashion_site_order_received_page import order_received_page


@pytest.mark.frontend
@pytest.mark.orderplace
class Test_order_placement:
    """
    This function consist of test cases:
    1. test_validate_user_is_able_to_place_order: to verify that user is able to place an order.

    2. test_validate_user_is_able_to_place_order_with_coupon: to verify that user
    is able to place an order with coupon code.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.home_page = fashion_site_home_page(self.driver)
        self.cart_page = fashion_site_cart_page(self.driver)
        self.checkout_page = fashion_site_checkout_page(self.driver)
        self.order_received_page = order_received_page(self.driver)

    def add_item_to_cart(self):
        self.home_page.go_to_home()
        self.home_page.add_products_to_cart()
        self.home_page.go_to_cart()
        self.cart_page.select_free_shipping_radio()
        self.cart_page.verify_free_shipping_selected()

    def place_order(self):
        self.cart_page.click_proceed_to_checkout_btn()
        self.checkout_page.verify_checkout_page_loaded()
        self.checkout_page.fill_details()
        self.checkout_page.place_order()
        self.order_received_page.verify_order_received()

    @pytest.mark.run(order=1)
    def test_validate_user_is_able_to_place_order(self):
        self.add_item_to_cart()
        self.place_order()

    @pytest.mark.run(order=2)
    def test_validate_user_is_able_to_place_order_with_coupon(self):
        self.add_item_to_cart()
        self.cart_page.apply_coupon_to_cart()
        self.place_order()
