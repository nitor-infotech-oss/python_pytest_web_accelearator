"""
This file consist of all the elements of My Account Page and the actions performed on it.
"""
from selenium.webdriver.common.by import By
from pytest_practical.tests.web_element.element_list import ElementList
import logging
from pytest_practical.tests.pages.base_page import BasePage

logger = logging.getLogger("root")


class my_account_fashion_site_page(BasePage):

    @property
    def Logout_link(self):
        return ElementList.LINK(
            self.driver, (By.XPATH,
                          '//a[text()="Logout"]'))

    @property
    def Account_details_link(self):
        return ElementList.LINK(
            self.driver,
            (By.XPATH,
             '//a[@href="http://mystore.local/my-account/edit-account/" and text()="Account details"]'))

    @property
    def password_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="password"]'))

    @property
    def username_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="username"]'))

    @property
    def login_button(self):
        return ElementList.BUTTON(
            self.driver,
            (By.CSS_SELECTOR, 'button[class="woocommerce-button button woocommerce-form-login__submit"]'))

    @property
    def register_password_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="reg_password"]'))

    @property
    def register_email_TEXTBOX(self):
        return ElementList.TEXTBOX(
            self.driver, (By.CSS_SELECTOR, 'input[id="reg_email"]'))

    @property
    def register_button(self):
        return ElementList.BUTTON(
            self.driver, (By.CSS_SELECTOR,
                          'button[class="woocommerce-Button woocommerce-button button woocommerce-form-register__submit"]'))

    @property
    def cartcontents_link(self):
        return ElementList.LINK(
            self.driver, (By.CSS_SELECTOR, 'a[class="cart-contents"]'))

    # ===================================================== actions ================================================== #

    def user_login(self, username, password):
        """
        This function is used for user login.
        :param username:
        :param password:
        :return:
        """
        self.username_TEXTBOX.enter_text(username)
        self.password_TEXTBOX.enter_text(password)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.login_button.click()

    def user_logout(self):
        """
        This function is used for logging out.
        :return:
        """
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.Logout_link.click()

    def valid_user_registration(self, email, password):
        """
        This function is used to validate user registration.
        :param email:
        :param password:
        :return:
        """
        logger.info("\n\n\t\tRegistering user........")
        logger.info("\n\t\tEmail: {}\n\t\tPassword: {}\n\n".format(email, password))
        self.register_email_TEXTBOX.enter_text(email)
        self.register_password_TEXTBOX.enter_text(password)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.register_button.click()

    def invalid_user_registration(self, email, password):
        """
        This function is used to verify invalid user registration
        :param email:
        :param password:
        :return:
        """
        self.register_email_TEXTBOX.enter_text(email)
        self.register_password_TEXTBOX.enter_text(password)
        try:
            if self.register_button.is_clickable() is False:
                logger.info("\n\nRegister Button Disabled : Please Enter Valid Username and Password\n\n")
        except:
            pass

    def verify_user_login(self):
        """
        This function is used to verify user login.
        :return:
        """
        if self.Account_details_link.is_displayed() and self.Logout_link.is_displayed():
            logger.info("\n\nLogin Successful!\n\n")

    def verify_user_registration(self):
        """
        This function is used to verify user registration
        :return:
        """
        self.verify_user_login()
        logger.info("\n\nUser Registration Successful!\n\n")

    def verify_login_or_registration_failed(self):
        """
        This function is user to verify failed login or registration.
        :return:
        """
        if self.login_button.is_element_visible():
            logger.info("\n\nPlease Enter Valid Credentials\n\n")
