"""
This file consist of test related to the failed cases.
"""
import pytest
from pytest_practical.tests.pages.my_account_fashion_site_page import my_account_fashion_site_page
from pytest_practical.tests.pages.fashion_site_home_page import fashion_site_home_page
from pytest_practical.data_providers.data_provider import DataProvider


@pytest.mark.frontend
@pytest.mark.login
class Test_login_fail:
    """
    This function consist of test cases:
    1. test_validate_user_is_not_able_to_login: to verify that user
        is not able to login upon entering wrong credentials.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        google_sheet_id = '1KWXC8u1baB_zl_JhC4BJiKL1JZTbB_uDljaIbx4FCNM'
        self.filename = self.directory + '\\python_pytest_web.json'
        self.google_sheet = DataProvider(google_sheet_id=google_sheet_id)
        self.home_page = fashion_site_home_page(self.driver)
        self.my_account = my_account_fashion_site_page(self.driver)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('user', ["admin_admin"])
    def test_validate_user_is_not_to_login(self, user):
        credentials = self.google_sheet.read_google_sheet_credentials(user=user)
        self.home_page.go_to_my_account()
        self.my_account.user_login(credentials['username'], credentials['password'])
        self.my_account.verify_user_login()
        self.my_account.user_logout()
