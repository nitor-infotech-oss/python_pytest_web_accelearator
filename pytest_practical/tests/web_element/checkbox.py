"""
Module defines the Checkbox functionality
"""
import logging
from distutils.util import strtobool

from pytest_practical.tests.web_element.base_element import BaseElement

logger = logging.getLogger("root")


class CheckBox(BaseElement):
    """
    Class defines Checkbox related functionality
    """

    def is_disabled(self):
        """
        Checking if checkbox is Disabled
        :return:
        """
        logger.debug("Checking if checkbox is Disabled")
        status = self.web_element.get_attribute("disabled")
        flag = False
        if status == 'true' or status == 'disabled':
            flag = True
        return flag

    def is_checked(self):
        """
        Checking if checkbox is checked
        :return:
        """
        self.hover()
        logger.debug("Checking if checkbox is checked")
        status = self.web_element.get_attribute("checked")
        logger.debug("Current State of Checkbox: {0}".format(status))
        flag = False
        if status == 'true' or status == 'checked':
            flag = True
        return flag

    def check(self):
        """
        Method to Check the checkbox
        :return:
        """
        logger.debug("Calling Check method")
        if not self.is_checked():
            self.click()

    def uncheck(self):
        """
        Method to Uncheck the checkbox
        :return:
        """
        logger.debug("Calling Uncheck method")
        if self.is_checked():
            self.click()

    def toggle(self):
        """
        Method to toggle check/uncheck from its previous state
        :return:
        """
        logger.debug("Calling Toggle method")
        self.click()

    def toggle_to_value(self, value):
        """
        Method to toggle check/uncheck on the basis of attribute named "value"
        :param value:
        :return:
        """
        logger.debug("Toggling to value:{0}".format(value))
        while self.get_attribute('value') != str(value):
            self.click()

    def toggle_to_state(self, state):
        """
        Method to toggle check/uncheck to its correct state
        :param state:
        :return:
        """
        logger.debug("Toggling to value:{0}".format(state))
        try:
            state = strtobool(str(state))
            if state:
                self.check()
            else:
                self.uncheck()
        except ValueError:
            logger.debug("Unrecognized State:{0} to Toggle Checkbox".format(state))
