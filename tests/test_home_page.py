import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_home import HomePage

from conftest import driver

@pytest.mark.usefixtures('driver')
class TestHomePage:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.home_page = HomePage(self.driver)

    def test_elements_displayed_on_the_screen(self):
        assert self.home_page.verifying_if_the_elements_are_displayed

    def test_creation_from_the_json_file(self):
        assert self.home_page.container_created_from_json()
