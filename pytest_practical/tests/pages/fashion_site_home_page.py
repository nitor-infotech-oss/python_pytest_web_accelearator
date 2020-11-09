"""
This file consist of all the elements of Home Page and the actions performed on it.
"""
from selenium.webdriver.common.by import By
from pytest_practical.tests.web_element.element_list import ElementList
import logging
from pytest_practical.tests.pages.base_page import BasePage
import time

logger = logging.getLogger("root")


class fashion_site_home_page(BasePage):

    @property
    def buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=20"]'))
    @property
    def product_hoodiewithlogo_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH,
                          '//a[@href="http://mystore.local/product/hoodie-with-logo/" and @class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]'))

    @property
    def addtocart13buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=13"]'))

    @property
    def search_textbox(self):
        return ElementList.TEXTBOX(
            self.driver, (By.ID, 'woocommerce-product-search-field-0'))

    @property
    def cart_contents_link(self):
        return ElementList.LINK(
            self.driver, (By.CSS_SELECTOR, 'a[class="cart-contents"]'))

    @property
    def addtocart23buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=23"]'))

    @property
    def product_beanie_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH,
                          '//a[@href="http://mystore.local/product/beanie/" and @class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]'))

    @property
    def addtocart16buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=16"]'))

    @property
    def product_tshirt_link(self):
        return ElementList.LINK(self.driver, (By.XPATH,
                                              '//a[@href="http://mystore.local/product/t-shirt/" and @class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]'))

    @property
    def addtocart22buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=22"]'))

    @property
    def product_hoodie_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH,
                          '//a[@class="woocommerce-LoopProduct-link woocommerce-loop-product__link" and @href="http://mystore.local/product/hoodie/"]'))


    @property
    def addtocart21buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=21"]'))

    @property
    def Home_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//*[@class="nav-menu"]//a[@href="http://mystore.local/"]'))

    @property
    def Myaccounthttpmystorelocalmyaccount_link(self):
        return ElementList.LINK(
            self.driver,
            (By.XPATH, '//*[@class="nav-menu"]//a[@href="http://mystore.local/my-account/"]'))

    @property
    def addtocart17buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=17"]'))

    @property
    def addtocart32buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=32"]'))

    @property
    def addtocart24buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=24"]'))

    @property
    def addtocart15buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH, '//a[@href="?add-to-cart=15"]'))

    @property
    def product_album_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH,
                          '//a[@href="http://mystore.local/product/album/" and @class="woocommerce-LoopProduct-link woocommerce-loop-product__link"]'))

    # =================================================== actions ==================================================== #

    def go_to_home(self):
        """
        This function is used to click on home page tab.
        :return:
        """
        self.Home_link.click()

    def add_products_to_cart(self):
        """
        This function is used to add products to cart from homepage.
        :return:
        """
        logger.info("\n\nAdding 5 items to cart\n\n")
        time.sleep(3)
        self.addtocart13buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link.click()
        self.addtocart15buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link.click()
        self.addtocart16buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link.click()
        self.addtocart17buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link.click()
        self.addtocart23buttonproducttypesimpleaddtocartbuttonajaxaddtocart_link.click()
        time.sleep(5)

    def go_to_cart(self):
        """
        This function is used to add products to cart from Home Page.
        :return:
        """
        logger.info("\n\nGoing to Shopping Cart\n\n")
        self.cart_contents_link.click()
        time.sleep(5)

    def search_products(self, search_item):
        """
        This function is used to search for the product on homepage
        :param search_item:
        :return:
        """
        time.sleep(3)
        logger.info("\n\nSearching for product {}.......\n\n".format(search_item))
        self.search_textbox.send_keys(search_item)
        self.search_textbox.press_enter_button()

        if search_item == 'hoodie':
            self.product_hoodie_link.click()
        elif search_item == 'beanie':
            self.product_beanie_link.click()
        elif search_item == 't shirt':
            self.product_tshirt_link.click()
        else:
            pass

    def go_to_my_account(self):
        """
        This function is used to go to MY ACCOUNT page.
        :return:
        """
        time.sleep(3)
        self.Myaccounthttpmystorelocalmyaccount_link.click()
