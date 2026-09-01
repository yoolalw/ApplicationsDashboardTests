import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page_home import PageHome
from tests.pages.page_homepage import PageHomePage

@allure.parent_suite("Web Tests - Applications Dashboard")
@allure.suite("Tests functions in HomePage")
@pytest.mark.usefixtures("driver")
class TestPageHomePage:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/internal-homepage')
        self.page_homepage = PageHomePage(self.driver)
        self.page_home = PageHome(self.driver)

    @allure.title("Verifying the displayed elements on screen")
    def test_verifying_displayed_elements(self):
        assert self.page_homepage.verifying_if_the_containers_has_been_present()

    @allure.title("Verifying all elements in containers (With Web link and Without Web link) ")
    def test_verifying_if_the_containers_have_elements_inside(self):
        assert self.page_homepage.verifying_elements_into_container_without_web_link() and self.page_homepage.verifying_elements_into_container_with_web_link()

    @allure.title("Verifying status changing after start the instance")
    def test_verifying_if_the_status_has_been_changed(self):
        assert self.page_homepage.verifying_if_the_status_has_been_changed_container_without() and self.page_homepage.verifying_if_the_status_has_been_changed_container_with()

    @allure.title("Click in 'Open' button and verifying redirect")
    def test_click_in_open_button_with_the_status_are_equal_running(self):
        self.page_homepage.click_in_button_open_application_with_web_link()
        assert self.wait.until(expected_conditions.url_changes("http://localhost:8080/auth/login"))

    @allure.title("Verifying if the message 'No web link' are present in container without web link")
    def test_verifying_message_if_the_container_dont_have_web_link(self):
        assert 'No web link' in self.page_homepage.checking_text_returned_from_container_without_web_link()

    @allure.title("Click in 'Open Control Panel' and checking if the url has been changed for the page Home")
    def test_click_and_returns_to_control_page(self):
        self.page_homepage.click_in_button_open_control_panel()
        assert self.page_home.verifying_elements_displayed_in_home()
