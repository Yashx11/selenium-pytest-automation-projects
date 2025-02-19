from pages.BasePage import BasePage
from pages.HomePage import HomePage
from Utils.readproperties import read_configurations
from TestCase.test_login import TestLogin

class TestHomePge:
    base_url = read_configurations("Basic Info", "base_url")

    def login(self, setup):
        self.driver = setup
        login = TestLogin()
        login.test_login(setup)

    def test_banner_slider_button(self,setup):
        self.driver = setup
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.banner_slider()

    def test_filter_phone_category_product(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.click_on_phone_category()

    def test_filter_laptop_category_product(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.click_on_laptop_category()

    def test_filter_monitor_category_product(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        home_page.click_on_monitor_category()