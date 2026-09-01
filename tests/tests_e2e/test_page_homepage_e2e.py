from time import sleep

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page_homepage import PageHomePage
from tests.pages.page_home import PageHome
from tests.conftest import driver

@allure.parent_suite("Web Tests - Applications Dashboard")
@allure.suite("Tests E2E -> Page HomePage")
@pytest.mark.usefixtures("driver")
class TestsPageHomePageE2E:
    driver: WebDriver
    wait: WebDriverWait
    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000')
        self.page_homepage = PageHomePage(self.driver)
        self.page_home = PageHome(self.driver)

    @allure.title("Test E2E -> Starting applications, verifying changes and redirecting to url added")
    def test_e2e_page_homepage(self):
        self.page_home.click_on_start_the_application_created()
        self.page_home.click_on_start_the_application_created()
        assert 'running' in self.page_home.verifying_status_from_created_container()

        self.page_home.click_in_sidebar_button_homepage_page()

        assert self.wait.until(expected_conditions.url_changes("http://127.0.0.1:3000/internal-homepage"))

        assert self.page_homepage.verifying_if_the_status_has_been_changed_container_with()
        self.page_homepage.click_in_button_open_application_with_web_link()
        assert self.wait.until(expected_conditions.url_changes('http://localhost:8080/auth/login'))
        self.driver.get("http://127.0.0.1:3000/internal-homepage")
        self.page_homepage.click_in_button_open_control_panel()
        assert self.page_home.verifying_elements_displayed_in_home()


