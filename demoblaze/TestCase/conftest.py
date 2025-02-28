import pytest
from selenium import webdriver
from Utils.Logger import logger
from Utils.readproperties import read_configurations

browser = read_configurations("Basic Info", "browser")

@pytest.fixture()
def setup():
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox()
    elif browser.lower() == "edge":
        driver = webdriver.Edge()
    else:
        return "Driver not Found"
    driver.maximize_window()
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_setup(item):
    logger.info(f"==== START TEST: {item.name} ====")
    yield

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item):
    yield
    logger.info(f"==== END TEST: {item.name} ====")
