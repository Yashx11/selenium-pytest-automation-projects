import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.click()

    def enter_value_in_element(self, xpath, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        element.clear()
        element.send_keys(value)

    def retrieve_js_alert_text(self):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def verify_js_alert_task(self, task):
        element = self.retrieve_js_alert_text()
        assert task == element

    def verify_task(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        assert element.is_displayed()

    def get_unique_user_name(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%d-%m-%Y-%H-%M-%S")
        username = f"User-{formatted_datetime}"
        return username


