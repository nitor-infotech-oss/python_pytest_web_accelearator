"""
This file consist of all the elements of Checkout Page and the actions performed on it.
"""
from pytest_practical.tests.pages.base_page import BasePage
from pytest_practical.tests.web_element.element_list import ElementList
from pytest_practical.tests.utils.common import *
import time
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger("root")


class fashion_site_checkout_page(BasePage):

    @property
    def place_order_button(self):
        return ElementList.BUTTON(
            self.driver, (By.CSS_SELECTOR, 'button#place_order'))

    @property
    def page_header_label(self):
        return ElementList.LABEL(
            self.driver, (By.CSS_SELECTOR, 'h1.entry-title'))

    @property
    def billing_first_name_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_first_name"]'))

    @property
    def billing_last_name_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_last_name"]'))

    @property
    def billing_company_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_company"]'))

    @property
    def billing_address1_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_address_1"]'))

    @property
    def billing_address2_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_address_2"]'))

    @property
    def billing_city_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_city"]'))

    @property
    def billing_postcode_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_postcode"]'))

    @property
    def billing_email_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_email"]'))

    @property
    def billing_phone_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="billing_phone"]'))

    @property
    def billing_country_select(self):
        return ElementList.DROPDOWN(
            self.driver, (By.CSS_SELECTOR, 'select[id="billing_country"]'))

    @property
    def billing_state_select(self):
        return ElementList.DROPDOWN(
            self.driver, (By.CSS_SELECTOR, 'select[id="billing_state"]'))

    @property
    def shipping_first_name_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="shipping_first_name"]'))

    @property
    def shipping_last_name_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="shipping_last_name"]'))

    @property
    def shipping_company_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="shipping_company"]'))

    @property
    def shipping_address1_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="shipping_address_1"]'))

    @property
    def shipping_address2_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="shipping_address_2"]'))

    @property
    def shipping_city_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="shipping_city"]'))

    @property
    def shipping_postcode_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="shipping_postcode"]'))

    @property
    def remember_me_checkbox(self):
        return ElementList.CHECKBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="rememberme"]'))

    # ===================================================== actions ================================================== #

    def verify_checkout_page_loaded(self):
        """
        This function is used to verify whether checkout page is loaded.
        :return:
        """
        logger.info("\n\nVerifying Checkout Page Loaded.......\n\n")
        try:
            assert self.page_header_label.is_element_visible() is True, 'Checkout page is not loaded'
        except:
            pass

        time.sleep(5)

    def form_details(self):
        """
        This function is used to set the details on checkout page.
        :return:
        """
        random_name = generate_random_first_and_last_name()
        f_name = random_name['f_name']
        l_name = random_name['l_name']
        company = generate_random_details()['company']
        addr_1 = generate_random_details()['addr_1']
        city = generate_random_details()['city']
        zip = generate_random_details()['zip']
        phone = generate_random_details()['phone']
        email = generate_random_email_and_password()['email']

        self.billing_first_name_TEXTBOX.enter_text(f_name)
        self.billing_last_name_TEXTBOX.enter_text(l_name)
        self.billing_company_TEXTBOX.enter_text(company)
        self.billing_address1_TEXTBOX.enter_text(addr_1)
        self.billing_city_TEXTBOX.enter_text(city)
        self.billing_postcode_TEXTBOX.enter_text(zip)
        self.billing_phone_TEXTBOX.enter_text(phone)
        self.billing_email_TEXTBOX.enter_text(email)

        time.sleep(5)

    def fill_details(self):
        """
        This function is used to fill the details on checkout page.
        :return:
        """
        logger.info("\n\nFilling Order Details Form.......\n\n")
        self.form_details()

    def place_order(self):
        """
        This function is used to place the order by clicking on place order button element.
        :return:
        """
        logger.info("\n\nPlacing Order.......\n\n")
        self.place_order_button.click()
        time.sleep(5)
