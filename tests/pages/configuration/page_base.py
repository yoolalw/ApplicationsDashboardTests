import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait


class PageBase:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def displayed(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).is_displayed()

    def fill(self, locator, value):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text