import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from tests.pages.page_home import PageHome
from tests.conftest import driver

@pytest.mark.usefixtures("driver")
class TestPageHome:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.page_home = PageHome(self.driver)

    #1
    def test_verifying_if_the_elements_are_displayed(self):
        assert self.page_home.verifying_elements_displayed_in_home()
    #2
    def test_verifying_existence_of_application_ping_test_internet(self):
        assert self.page_home.verifying_if_ping_teste_internet_application_has_been_displayed()
    #3
    def test_switching_the_language_of_website(self):
        self.page_home.switch_system_language()
        assert True
    #4
    def test_click_and_open_container_new_application(self):
        self.page_home.click_on_new_app_button()
        #5
        self.page_home.creating_new_application('App_Local_Test', '8080', 'C:\Blooms\BloomsKimono\jvApi', 'mvn', 'spring-boot:run')
        self.page_home.click_in_new_app_add_app_button()
        assert self.page_home.verifying_if_the_container_has_been_created()

    #6
    def test_starting_the_application_created(self):
        self.page_home.click_on_start_the_application_created()
        self.page_home.click_on_start_the_application_created()
        assert 'running' in self.page_home.verifying_status_from_created_container()

    #7
    def test_change_configuration_from_the_container_created(self):
        self.page_home.click_configurations_from_the_container_created()
        self.page_home.changes_configuration_from_the_container_created('New Name', '8080', 'C:\ryuSa\RyuFront\RyuStockSA', 'npx', 'live-server --port=2210')
        self.page_home.click_in_new_app_add_app_button()
        assert True

    #8
    def test_starting_the_application_with_new_configuration(self):
        self.page_home.click_on_start_the_application_created()
        self.page_home.click_on_start_the_application_created()
        assert 'running' in self.page_home.verifying_status_from_created_container()

    #9
    def test_verifying_if_the_alert_has_been_generated(self):
        self.page_home.click_on_new_app_button()
        self.page_home.creating_new_application('Application With Error', '2222', 'wrong', 'wrong', 'wrong')
        self.page_home.click_in_new_app_add_app_button()
        self.page_home.click_on_start_button_for_application_with_wrong_application()
        assert self.page_home.verifying_status_from_container_with_error_configuration()
        self.page_home.click_in_alert_icon()
        assert self.page_home.verifying_if_the_alert_has_been_generated()
        #10
        self.page_home.click_to_mark_all_alerts_read()
        #11
        self.page_home.click_to_clear_all_container_from_alerts()
        assert 'No alerts recorded' in self.page_home.verifying_text_from_alerts_container()