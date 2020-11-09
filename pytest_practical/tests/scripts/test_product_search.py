"""
@pytest.mark is used to mark a test with a particular tag
for eg: @pytest.mark.frontend, @pytest.mark.productsearch

@pytest.mark.parametrize is used to mark a test case as parameterize
and parameters can be passed in it.

@pytest.mark.run is used to mark a test in a particular order
for eg: @pytest.mark.run(order=1) to run the test case first

This test file consist of test cases related to product search.
"""
import pytest
from pytest_practical.tests.pages.fashion_site_home_page import fashion_site_home_page
from pytest_practical.data_providers.data_provider import DataProvider


@pytest.mark.frontend
@pytest.mark.productsearch
class Test_product_search:
    """
    This function consist of test cases:
    1. test_validate_user_is_able_to_search_product: to verify that user
        is able to search for products.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        google_sheet_id = '1KWXC8u1baB_zl_JhC4BJiKL1JZTbB_uDljaIbx4FCNM'
        self.google_sheet = DataProvider(google_sheet_id=google_sheet_id)
        self.home_page = fashion_site_home_page(self.driver)

    @pytest.mark.parametrize('search_item',
                             ["logo collection", "hoodie", "cap", "t shirt", "v neck", "hoodie with logo",
                              "beanie with logo",
                              "hoodie with zipper", "belt", "album"])
    def test_validate_user_is_able_to_search_product(self, search_item):
        self.home_page.search_products(search_item)
