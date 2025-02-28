import pytest
from selenium import webdriver
from Utils.Logger import logger

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
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
