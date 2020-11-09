from pytest_practical.tests.web_element.base_element import BaseElement
import logging
logger = logging.getLogger("root")


class RadioButton(BaseElement):

    def select(self):
        logger.debug("Calling select method")
        self.web_element.click()

    def is_selected(self):
        return self.web_element.is_selected()

