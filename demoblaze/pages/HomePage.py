import time
from pages.BasePage import BasePage

class HomePage(BasePage):
    sign_up_xpath = "//a[text()='Sign up']"
    login_xpath = "//a[text()='Log in']"
    cart_xpath = "//a[text()='Cart']"
    about_us_xpath = "//a[text()='About us']"
    contact_us_xpath = "//a[text()='Contact']"
    sign_up_user_name_input_xpath = "//input[@id='sign-username']"
    sign_up_password_input_xpath = "//input[@id='sign-password']"
    sign_up_button_xpath = "//button[text()='Sign up']"
    login_username_xpath = "//input[@id='loginusername']"
    login_password_xpath = "//input[@id='loginpassword']"
    login_button_xpath = "//button[text()='Log in']"
    same_username_validation_message = "This user already exist."
    sign_up_success_message = "Sign up successful."
    login_success_xpath = "//a[@id='nameofuser']"
    user_not_exist_message = "User does not exist."
    invalid_password_message = "Wrong password."
    banner_slider_left_button_xpath = "//span[@class='carousel-control-prev-icon']"

    def signup(self, username, password, task):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.sign_up_xpath)
        base_page.enter_value_in_element(self.sign_up_user_name_input_xpath, username)
        base_page.enter_value_in_element(self.sign_up_password_input_xpath, password)
        base_page.click_on_element(self.sign_up_button_xpath)
        time.sleep(2)
        base_page.verify_js_alert_task(task)

    def login(self, username, password):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.login_xpath)
        base_page.enter_value_in_element(self.login_username_xpath, username)
        base_page.enter_value_in_element(self.login_password_xpath, password)
        base_page.click_on_element(self.login_button_xpath)
        time.sleep(2)

    def banner_slider(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element(self.banner_slider_left_button_xpath)

    def click_on_phone_category(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element("//a[text()='Phones']")

    def click_on_laptop_category(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element("//a[text()='Laptops']")

    def click_on_monitor_category(self):
        base_page = BasePage(self.driver)
        base_page.click_on_element("//a[text()='Monitors']")
