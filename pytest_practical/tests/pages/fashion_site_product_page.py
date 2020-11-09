"""
This file consist of all the elements of Product Page and the actions performed on it.
"""
from pytest_practical.tests.web_element.element_list import ElementList
from pytest_practical.tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import time

logger = logging.getLogger("root")


class fashion_site_product_page(BasePage):

    @property
    def cart_content_link(self):
        return ElementList.LINK(self.driver, (By.CSS_SELECTOR, 'a[class="cart-contents"]'))

    @property
    def add_to_cart_button(self):
        return ElementList.BUTTON(
            self.driver, (By.CSS_SELECTOR, 'button[class="single_add_to_cart_button button alt"]'))

    @property
    def select_color_dropdown(self):
        return ElementList.DROPDOWN(
            self.driver, (By.ID, 'pa_color'))

    @property
    def select_size_dropdown(self):
        return ElementList.DROPDOWN(
            self.driver, (By.ID, 'pa_size'))

    @property
    def logo_option_dropdown(self):
        return ElementList.DROPDOWN(
            self.driver, (By.ID, 'logo'))

    @property
    def not_found_label(self):
        return ElementList.LABEL(self.driver, (
            By.XPATH, '//p[@class="woocommerce-info"]'))

    # ===================================================== actions ===================================================#
    def add_to_cart(self, item, color=None, option=None):
        """
        This function is used to add particular product to cart.
        :param item:
        :param color:
        :param option:
        :return:
        """
        time.sleep(3)

        if item == 'hoodie' or item == 'v neck':
            logger.info("\n\nProduct Found!\nAdding {} to cart.......\n\n".format(item))
            if item == 'hoodie':
                if color is None or option is None:
                    self.select_color_dropdown.select_by_value("blue")
                    self.logo_option_dropdown.select_by_value("No")
                    self.add_to_cart_button.click()
                else:
                    self.select_color_dropdown.select_by_value(color)
                    self.logo_option_dropdown.select_by_value(option)
                    self.add_to_cart_button.click()

            elif item == 'v neck':
                if color is None or option is None:
                    self.select_color_dropdown.select_by_value("red")
                    self.select_size_dropdown.select_by_value("large")
                    self.add_to_cart_button.click()
                else:
                    self.select_color_dropdown.select_by_value(color)
                    self.select_size_dropdown.select_by_value(option)
                    self.add_to_cart_button.click()

        else:
            logger.info("\n\nProduct Found!\nAdding {} to cart.......\n\n".format(item))
            self.add_to_cart_button.click()
