from pytest_practical.tests.web_element.base_element import BaseElement
import logging
logger = logging.getLogger("root")


class Link(BaseElement):

    def get_href_link(self):
        logger.debug("Getting hyperlink value")
        return self.web_element.get_attribute("href")
