import time

from pages.BasePage import BasePage
from pages.HomePage import HomePage
from Utils.readproperties import read_configurations
from selenium.webdriver.common.alert import Alert

class TestLogin:
    base_url = read_configurations("Basic Info", "base_url")
    username = read_configurations("Basic Info", "username")
    password = read_configurations("Basic Info", "password")

    def test_sign_up_already_exist_user(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.signup("Demo" ,"Demo", home_page.same_username_validation_message)

    def test_signup_with_fresh_account(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.signup(self.username, self.password, home_page.sign_up_success_message)

    def test_login_with_invalid_details(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        home_page.login(878872, self.password)
        base_page.verify_js_alert_task(home_page.user_not_exist_message)

    def test_login_with_valid_user_invalid_password(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        home_page.login(self.username, 487878787)
        base_page.verify_js_alert_task(home_page.invalid_password_message)

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        base_page = BasePage(self.driver)
        home_page = HomePage(self.driver)
        home_page.login(self.username, self.password)
        base_page.verify_task(home_page.login_success_xpath)
