"""This module defines the newly designed BasePage class.
Class name and file name will be updated later, once this is ready to be merged"""

import logging

from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger("root")


class BasePage(object):
    def __init__(self, app):
        """Constructor"""
        self._app = app
        self.driver = self._app
        self.driver.set_page_load_timeout(120)
        self.wait = WebDriverWait(self.driver, 15)
        self.short_wait = WebDriverWait(self.driver, 2)
        self.medium_wait = WebDriverWait(self.driver, 4)
