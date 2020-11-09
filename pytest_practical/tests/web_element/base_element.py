"""
Module for defining ``BaseElement`` class which will be then derived on other element classes
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

import logging

logger = logging.getLogger("root")


class BaseElement(object):
    """
    This class defines the basic element class with all generic properties and methods defined


    """

    def __init__(self, driver, selector, wait_time=10):
        """
        Constructor to initialize BaseElement and any Dervied element classes unless overridden

        :param driver: Required
                Type is selenium.webdriver.remote.webdriver.WebDriver
        :param selector: Required.
                Type is string, tuple or WebElement instance. if it is tuple, the first param in tuple should be
                selector_type listed by `selenium.webdriver.common.by.By` and second param should be selector value.
                if it is string, it should be some name (id, name, class name, tag name, link or partial link text)
        :param wait_time: Optional
        """

        logger.debug(
            "Initialize class: {0} with selector {1}:".format(
                self.__class__.__name__, selector))
        self._selector = selector
        self._driver = driver
        self._wait = WebDriverWait(self._driver, wait_time)

    @property
    def selector(self):
        return self._selector

    @property
    def web_element(self):
        """ Property to return element set on constructor or found via unique selector value, string
        if element value is set then that is returned else element is searched via locator strategies
        """
        logger.debug("Calling web_element property")
        if isinstance(self._selector, tuple):
            return self._wait_until_clickable()
        elif isinstance(self._selector, str):
            return self._find_element_possibilities()
        elif isinstance(self._selector, WebElement):
            return self._selector
        else:
            raise Exception("Incorrect selector format")

    @property
    def web_elements(self):
        """
        This property returns all the web elements found using the selector.
        :return:
        """
        if isinstance(self._selector, tuple):
            return self._driver.find_elements(*self._selector)

    @property
    def element(self):
        """
        This property returns any element which matches the selector. It is different to the web_element
        such that it returns any HTML element. Used typically when elements are not displayed in the UI
        :return:
        """
        if isinstance(self._selector, tuple):
            return self._driver.find_element(*self._selector)

    def _wait_until_clickable(self):
        try:
            logger.debug(
                "Finding element with selector:{0}".format(
                    self._selector))
            return self._wait.until(EC.element_to_be_clickable(self._selector))
        except TimeoutException as e:
            logger.debug("Unable to Find element with selector: {0}".format(self._selector))
            logger.debug(e.msg)
            return False

    def _find_element_possibilities(self):
        """
        This will search for unique element possibilities for locator string wich could be any text
        but locator types are not defined.
        Locator precedence is Id > Name > Linktext > Partial Linktext > Tag Name > class name
        """
        logger.debug(
            "Finding element possibilities with selector string:{0}".format(self._selector))
        possible_elements = []
        strategies = [
            By.CSS_SELECTOR,
            By.ID,
            By.CLASS_NAME,
            By.LINK_TEXT,
            By.PARTIAL_LINK_TEXT,
            By.TAG_NAME,
            By.XPATH,
            By.NAME]
        for strategy in strategies:
            try:
                logger.debug("Strategy:{0}".format(strategy))
                possible_elements.append(
                    self._driver.find_element(
                        strategy, self._selector))
            except NoSuchElementException as e:
                logger.debug(
                    "Not found using Strategy:{0}. Exception:{1}".format(
                        strategy, e))
            logger.debug(possible_elements)
        if len(possible_elements) == 1:
            return possible_elements[0]
        else:
            raise Exception(
                "No unique element found using smart search for selector: {0}".format(
                    self._selector))

    def click(self):
        logger.debug("Performing click")
        self.hover()
        self.web_element.click()

    def right_click(self):
        logger.debug("Performing right click")
        self.web_element.context_click()

    def hover(self):
        logger.debug("Performing hover action")
        mouse = ActionChains(self._driver)
        mouse.move_to_element(self.web_element).perform()

    @property
    def text(self):
        """Defined as property as underlying WebElement class has this as exposed as property"""
        logger.debug("Getting text property")
        return self.web_element.text

    @property
    def texts(self):
        """
        Returns the text of the web elements
        :return:
        """
        return [elem.text for elem in self.web_elements]

    def is_displayed(self):
        logger.debug("Checking if element is displayed")
        return self.web_element.is_displayed()

    def is_enabled(self):
        logger.debug("Checking if element is enabled")
        return self.web_element.is_enabled()

    def is_element_visible(self):
        """
        Checks if element is visible and returns True or False
        """
        if self.web_element.is_displayed():
            return True
        else:
            return False

    def is_element_enabled(self):
        """
        Checks if element is enabled and returns True or False
        """
        if self.web_element.is_enabled():
            return True
        else:
            return False

    def get_attribute(self, attribute, not_web_element=False):
        if not_web_element:
            element = self.element
        else:
            element = self.web_element
        value = element.get_attribute(attribute)
        logger.debug(
            "Getting attribute:{0} with Value:{1}".format(
                attribute, value))
        return value

    def is_clickable(self):
        logger.debug("Checking if element is clickable")
        try:
            return self._wait.until(
                EC.element_to_be_clickable(self.web_element))
        except BaseException:
            return False
