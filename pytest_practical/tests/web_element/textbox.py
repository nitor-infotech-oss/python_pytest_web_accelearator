from pytest_practical.tests.web_element.base_element import BaseElement
from selenium.webdriver.common.keys import Keys
import time

import logging

logger = logging.getLogger("root")


class TextBox(BaseElement):

    def press_enter_button(self):
        logger.debug("Pressing Enter Button")
        self.web_element.send_keys(Keys.ENTER)

    def enter_text(self, input_text):
        logger.debug("Clear and Enter text")
        self.clear()
        time.sleep(2)
        self.click()
        self.send_keys(keys=input_text)

    def send_keys(self, keys):
        logger.debug("Pressing keys")
        self.click()
        self.web_element.send_keys(keys)

    def clear(self):
        logger.debug("Clearing Textbox")
        self.web_element.clear()

    def clear_delete(self):
        logger.debug("Clearing Textbox")
        self.web_element.send_keys(Keys.ESCAPE)
        time.sleep(2)
        self.web_element.send_keys(Keys.DELETE)
        self.web_element.clear()

    def clear_with_backspace(self):
        logger.debug("Clearing Textbox")
        count = len(self.web_element.get_attribute("value"))
        self.web_element.click()
        time.sleep(2)
        while count > 0:
            self.web_element.send_keys(Keys.BACKSPACE)
            count -= 1
