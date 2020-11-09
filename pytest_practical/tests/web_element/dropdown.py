"""
Module defines the Class for the DropDown Web Element
"""
import logging
from pytest_practical.tests.web_element.base_element import BaseElement
from selenium.webdriver.support.select import Select

LOGGER = logging.getLogger("root")


class DropDown(BaseElement):
    """
    Class Defines the functionalities of the Dropdown Web Element
    """

    @property
    def web_element(self):
        if isinstance(self._selector, tuple):
            return Select(self._wait_until_clickable())
        elif isinstance(self._selector, str):
            return Select(self._find_element_possibilities())
        else:
            raise Exception("Incorrect selector format")

    def select_by_index(self, index):
        """
        Method selects the option based on the index
        :param index:
        :return:
        """
        LOGGER.debug("select by index:{0}".format(index))
        self.web_element.select_by_index(index)

    def select_by_value(self, value):
        """
        Method selects the option based on its actual value
        :param value:
        :return:
        """
        LOGGER.debug("select by value:{0}".format(value))
        self.web_element.select_by_value(value)

    def select_by_visible_text(self, text):
        """
        Method selects the options based on the text that is visible
        :param text:
        :return:
        """
        LOGGER.debug("select by visible text:{0}".format(text))
        if self.web_element:
            self.web_element.select_by_visible_text(text)

    def deselect_by_index(self, index):
        """
        Method deselects the options based on its index value
        :param index:
        :return:
        """
        LOGGER.debug("deselect by index:{0}".format(index))
        self.web_element.deselect_by_index(index)

    def deselect_by_value(self, value):
        """
        Method deselects the option based on its actual value
        :param value:
        :return:
        """
        LOGGER.debug("deselect by index:{0}".format(value))
        self.deselect_by_value(value)

    def deselect_by_visble_text(self, text):
        """
        Method deselects the options based on the text that is visible
        :param text:
        :return:
        """
        LOGGER.debug("deselect by visible text:{0}".format(text))
        self.deselect_by_visble_text(text)

    def is_multiple_selection_allowed(self):
        """
        Method returns True if it is a Multi select dropdown
        :return:
        """
        LOGGER.debug("Check if multiple selection is allowed")
        self.web_element.is_multiple()

    def get_all_selected_options(self):
        """
        Methods returns the list of all selected options
        :return:
        """
        LOGGER.debug("Get all selected options")
        return self.web_element.all_selected_options

    def get_all_options(self):
        """
        Method returns a list of all options
        :return:
        """
        LOGGER.debug("Get all options")
        return self.web_element.options

    def deselect_all(self):
        """
        Method deslects all the selected options
        :return:
        """
        LOGGER.debug("Deselect all")
        self.web_element.deselect_all()

    def first_selected_option(self):
        """
        Method returns the currently selected option
        :return:
        """
        LOGGER.debug("Get first selected option (currently selected option)")
        return self.web_element.first_selected_option

    def first_selected_option_text(self):
        elem = self.first_selected_option()
        if elem:
            return elem.text
