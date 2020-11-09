"""
@pytest.mark is used to mark a test with a particular tag
for eg: @pytest.mark.frontend, @pytest.mark.login

@pytest.mark.parametrize is used to mark a test case as parameterize
and parameters can be passed in it.

@pytest.mark.run is used to mark a test in a particular order
for eg: @pytest.mark.run(order=1) to run the test case first

This test file consist of test cases related to user login.
"""
import pytest
from pytest_practical.tests.pages.my_account_fashion_site_page import my_account_fashion_site_page
from pytest_practical.tests.pages.fashion_site_home_page import fashion_site_home_page
from pytest_practical.data_providers.data_provider import DataProvider
from pytest_practical.data_providers import json_parser


@pytest.mark.frontend
@pytest.mark.login
class Test_login:
    """
    This function consist of test cases:
    1. test_validate_user_is_not_able_to_login: to verify that user
        is not able to login upon entering wrong credentials.

    2. test_validate_user_is_able_to_login: to verify that user
        is able to login upon entering right credentials.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        google_sheet_id = '1KWXC8u1baB_zl_JhC4BJiKL1JZTbB_uDljaIbx4FCNM'
        self.filename = self.directory + '\\python_pytest_web.json'
        self.google_sheet = DataProvider(google_sheet_id=google_sheet_id)
        self.home_page = fashion_site_home_page(self.driver)
        self.my_account = my_account_fashion_site_page(self.driver)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('user', ["wrong_user"])
    def test_validate_user_is_not_able_to_login(self, user):
        credentials = self.google_sheet.read_google_sheet_credentials(user=user)
        self.home_page.go_to_my_account()
        self.my_account.user_login(credentials['username'], credentials['password'])
        self.my_account.verify_login_or_registration_failed()

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('user', ["super_admin"])
    def test_validate_user_is_able_to_login(self, user):
        credentials = self.google_sheet.read_google_sheet_credentials(user=user)
        self.home_page.go_to_my_account()
        self.my_account.user_login(credentials['username'], credentials['password'])
        self.my_account.verify_user_login()
        self.my_account.user_logout()

    """
    This test is marked as xfail to display unexpected passes and expected fails in the pytest html-report.
    """
    @pytest.mark.run(order=3)
    @pytest.mark.xfail(reason="Expected Failed to login")
    @pytest.mark.parametrize('user', ["test_user_nitor", "super_admin", "admin"])
    def test_validate_user_is_able_to_login_with_json(self, user):
        credentials = json_parser.read_json_by_key(inputfile=self.filename, key=user)
        self.home_page.go_to_my_account()
        self.my_account.user_login(credentials['username'], credentials['password'])
        self.my_account.verify_user_login()
        self.my_account.user_logout()

    """
    This test is marked as skip to display skipped tests in the pytest html-report.
    """

    @pytest.mark.skip(reason="To Display skipped test in reports")
    def test_this_is_skipped(self):
        self.home_page = fashion_site_home_page(self.driver)
