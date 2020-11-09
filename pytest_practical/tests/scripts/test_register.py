"""
@pytest.mark is used to mark a test with a particular tag
for eg: @pytest.mark.frontend, @pytest.mark.register

@pytest.mark.parametrize is used to mark a test case as parameterize
and parameters can be passed in it.

@pytest.mark.run is used to mark a test in a particular order
for eg: @pytest.mark.run(order=1) to run the test case first

This test file consist of test cases related to user registration.
"""
import pytest
from pytest_practical.tests.pages.my_account_fashion_site_page import my_account_fashion_site_page
from pytest_practical.tests.pages.fashion_site_home_page import fashion_site_home_page
from pytest_practical.data_providers.data_provider import DataProvider
from pytest_practical.tests.utils import common


@pytest.mark.frontend
@pytest.mark.register
class Test_register:
    """
    This function consist of test cases:
    1. test_invalid_user_is_not_able_to_register: to verify that user
        is not able to register upon entering wrong credentials.

    2. test_valid_user_is_able_to_register: to verify that user
        is able to register upon entering right credentials.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        google_sheet_id = '1KWXC8u1baB_zl_JhC4BJiKL1JZTbB_uDljaIbx4FCNM'
        self.google_sheet = DataProvider(google_sheet_id=google_sheet_id)
        self.home_page = fashion_site_home_page(self.driver)
        self.my_account = my_account_fashion_site_page(self.driver)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('user', ["wrong_user"])
    def test_invalid_user_is_not_able_to_register(self, user):
        credentials = self.google_sheet.read_google_sheet_credentials(user=user)

        self.home_page.go_to_my_account()
        self.my_account.invalid_user_registration(credentials['username'], credentials['password'])
        self.my_account.verify_login_or_registration_failed()

    @pytest.mark.run(order=2)
    def test_valid_user_is_able_to_register(self):
        email = common.generate_random_email_and_password()['email']
        password = common.generate_random_email_and_password()['password']

        self.home_page.go_to_my_account()
        self.my_account.valid_user_registration(email, password)
        self.my_account.verify_user_registration()
        self.my_account.user_logout()
