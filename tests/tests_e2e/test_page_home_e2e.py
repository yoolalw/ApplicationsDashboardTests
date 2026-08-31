from time import sleep

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver
from tests.pages.page_home import PageHome


@allure.parent_suite('Web Tests - Applications Dashboard')
@allure.suite('Test E2E in Home page.')
@pytest.mark.usefixtures("driver")
class TestHomeE2E:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.page_home = PageHome(self.driver)

    @allure.title('Flux of tests E2E - HID: HTU01')
    def test_user_creating_new_applications_in_website(self):
        self.page_home.click_in_languages_button()
        self.page_home.click_to_change_language_for_portuguese()
        self.page_home.click_on_new_app_button()
        self.page_home.creating_new_application('Starting java application', '80', 'C:\Blooms\BloomsKimono\jvApi',
                                                'mvn', 'spring-boot:run')
        self.page_home.click_in_new_app_add_app_button()
        self.page_home.click_on_start_the_application_created()
        self.page_home.click_on_start_the_application_created()
        self.wait.until(
            expected_conditions.text_to_be_present_in_element(self.page_home.container_created_status, 'running'))

        self.page_home.click_on_start_the_application_created()
        self.page_home.click_configurations_from_the_container_created()
        self.page_home.changes_configuration_from_the_container_created('New application', '8080',
                                                                        'C:\Blooms\BloomsKimono\jvApi',
                                                                        'spring/boot-run', 'mvl')
        self.page_home.click_in_new_app_add_app_button()
        self.page_home.click_in_start_application_after_changes()
        self.wait.until(expected_conditions.text_to_be_present_in_element(self.page_home.container_created_status, 'failed'))
        self.page_home.click_in_alert_icon()
        self.page_home.verifying_if_the_alert_has_been_generated()
        self.page_home.click_to_mark_all_alerts_read()
        self.page_home.click_to_clear_all_container_from_alerts()
        assert 'Nenhum alerta registrado.' in self.page_home.verifying_text_from_alerts_container()
