"""
This file consist of all the elements of Order Received Page and the actions performed on it.
"""
from pytest_practical.tests.web_element.element_list import ElementList
from pytest_practical.tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import logging
import time

logger = logging.getLogger("root")


class order_received_page(BasePage):

    @property
    def thank_you_label(self):
        return ElementList.LABEL(
            self.driver, (By.CSS_SELECTOR, 'div.woocommerce-order p.woocommerce-thankyou-order-received'))
    # ===================================================== actions ================================================== #

    def verify_order_received(self):
        """
        This function is used to verify that the order is received.
        :return:
        """
        time.sleep(15)
        if self.thank_you_label.is_element_visible():
            logger.info("\n\nOrder Received\n\n")
        else:
            logger.info("\n\nFailed to place Order\n\n")
