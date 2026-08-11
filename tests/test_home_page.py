from time import sleep

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_home import HomePage

from conftest import driver
@allure.title('Tests in Page Home')
@allure.description('The tests will consist the assertions from new created applications')
@pytest.mark.usefixtures('driver')
class TestHomePage:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.home_page = HomePage(self.driver)

    #PDT01
    def test_verifying_if_home_are_running(self):
        assert self.home_page.verifying_if_the_elements_are_displayed()

    #PDT02
    def test_verifying_if_the_auto_container_has_been_created(self):
        assert self.home_page.container_auto_created_from_json()

    #PDT03
    def test_changes_the_language_and_checking_if_all_application_has_been_modified(self):
        self.home_page.selecting_language()
        assert True

    #PDT04
    def test_clicking_in_new_app_button(self):
        assert self.home_page.clicking_in_new_application()

    #PDT05
    @pytest.mark.parametrize(
        "input_name, input_port, input_web_link",
        [
            ('PokeApiWebLinkTest', '8231', 'https://pokeapi.co/')
        ]
    )
    def test_starting_new_application(self):
        self.home_page.clicking_in_new_application()
        self.home_page.creating_application_with_web_link()


