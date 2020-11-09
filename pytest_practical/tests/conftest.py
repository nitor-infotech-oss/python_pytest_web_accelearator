"""
This is the configuration file for Pytest solution and it contains
different runtime parameters.

We can also define universal fixtures which can be used across project.
"""
from msedge.selenium_tools import Edge, EdgeOptions
import pytest
from selenium import webdriver
import os
import logging
from datetime import datetime
from py.xml import html
from pytest_practical.data_providers import logger_util

logger = logging.getLogger("root")

root_dir = os.getcwd()
os.chdir(root_dir)
main_project_dir = os.getcwd()


@pytest.yield_fixture(scope="class")
def setup(request, env, browser, headless, log_level):
    """
    This function is used as a fixture to set the value for browser, headless, log_level, and env.

    in pytest 2.4 and above, we yield is used instead of return statement
    to provide a fixture value while otherwise fully supporting all other fixture features.
    :param request:
    :param env:
    :param browser:
    :param headless:
    :param log_level:
    :return:
    """
    global logger
    global driver

    logger = logger_util.log_message(log_level, "root")
    base_url = 'http://mystore.local/'
    test_data_dir = main_project_dir + '\\testdata'
    directory = test_data_dir + '\\' + env

    switcher = {
        "ie": get_ie_driver,
        "chrome": get_chrome_driver,
        "edge": get_edge_driver,
        "firefox": get_firefox_driver
    }
    driver = switcher[browser.lower()](headless)
    driver.implicitly_wait(3)
    if headless != 'true':
        driver.maximize_window()
    driver.get(base_url)

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.directory = directory

    yield driver, directory

    driver.quit()


def pytest_addoption(parser):
    """
    This function is used to add various parameters which is used for test execution.
    :param parser:
    :return:
    """
    parser.addoption("--browser", action="store", default="edge", help="Browser to use")
    parser.addoption("--env", help="Choose environment 'dev/qa/stage'", default="qa")
    parser.addoption("--headless", help="Whether to run in headless or not", default="true")
    parser.addoption("--log_level", help="Set the level of logging", default="INFO")


@pytest.fixture(scope="session")
def browser(request):
    """
    Fixture to set the value for browser.
    :param request:
    :return:
    """
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def log_level(request):
    """
    Fixture to set the value for log_level.
    :param request:
    :return:
    """
    return request.config.getoption("--log_level")


@pytest.fixture(scope="session")
def env(request):
    """
    Fixture to set the value for env.

    :param request:
    :return:
    """
    return request.config.getoption("--env")


@pytest.fixture(scope="session")
def headless(request):
    """
    Fixture to set the value for headless.
    :param request:
    :return:
    """
    return request.config.getoption("--headless")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = str(file_name).split("/")[-1]
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    """
    Funtion to take the screenshot of failed tests.
    :param name:
    :return:
    """
    driver.get_screenshot_as_file(name)


def get_chrome_driver(headless):
    """
    Function to return the instance of Chrome Driver.
    :param headless:
    :return:
    """
    chrome_options = webdriver.ChromeOptions()
    if str(headless).lower() == 'true':
        logger.info("\nRunning Test on Headless Chrome......\n")
        chrome_options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(options=chrome_options)

    return chrome_driver


def get_ie_driver():
    """
    Function to return the instance of IE Driver.
    :return:
    """
    logger.info("\nRunning Test Internet explorer......\n")
    ie_options = webdriver.IeOptions()
    ie_options.ignore_zoom_level = True
    ie_options.ignore_protected_mode_settings = True
    ie_driver = webdriver.Ie(ie_options=ie_options)
    return ie_driver


def get_firefox_driver(headless):
    """
    Function to return the instance of Firefox Driver.
    :param headless:
    :return:
    """
    ff_options = webdriver.FirefoxOptions()

    if str(headless).lower() == 'true':
        logger.info("\nRunning Test on Headless Firefox......\n")
        ff_options.add_argument('-headless')
    ff_driver = webdriver.Firefox(firefox_options=ff_options)

    return ff_driver


def get_edge_driver(headless):
    """
    Function to return the instance of Edge Driver.
    :param headless:
    :return:
    """
    edge_options = EdgeOptions()
    edge_options.use_chromium = True

    if str(headless).lower() == 'true':
        logger.info("\nRunning Test on Headless EDGE......\n")

        edge_options.add_argument("headless")
        edge_options.add_argument("disable-gpu")
    edge_driver = Edge(options=edge_options)

    return edge_driver


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.now(), class_='col-time'))
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
