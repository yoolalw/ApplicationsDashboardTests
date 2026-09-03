from time import sleep

import allure
import pytest
from allure_commons.types import Severity
from selenium.webdriver.common.devtools.v143.audits import disable
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver
from tests.pages.configuration.page_configuration import PageConfiguration
from tests.pages.page_home import PageHome


@allure.parent_suite("Web Tests -> Applications Dashboard")
@allure.suite("Interface Tests in Configuration Page")
@pytest.mark.usefixtures("driver")
class TestsPageConfiguration:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.page_home = PageHome(self.driver)
        self.page_home.click_in_sidebar_button_configurations_page()
        self.page_configuration = PageConfiguration(self.driver)

    # Tests -> Enabled/Disabled Apps Section!
    @allure.id("CED01")
    @allure.title("Verifying if the container exists")
    def test_verifying_if_the_container_are_displayed(self):
        assert self.page_configuration.section_enable.verifying_displayed_container()

    @allure.id("CED02")
    @allure.title("Click in button to disable the instance and verifying the status is equal 'Disabled'")
    def test_click_in_button_to_disable_instance(self):
        self.page_configuration.section_enable.click_in_button_disable()
        assert "Disabled" in

    @allure.id("CED03")
    @allure.title('Click in button to enable the instance and verifying if the status is equal \'Enabled\'')
    def test_click_in_button_to_enable_instance(self):
        self.page_configuration.section_enable.click_in_button_disable()
        assert 'Enabled' in self.page_configuration.section_enable.check_text_returned()

    @allure.id("CED04")
    @allure.title("Click in button to edit the element and verifying if the name, commands and arguments has been modified")
    def test_inserting_new_values_in_container_fields(self):
        self.page_configuration.section_enable.click_in_button_edit()
        self.page_configuration.section_enable.insert_new_values_in_app_name("New Name")
        self.page_configuration.section_enable.insert_new_values_in_command("ipconfig")
        self.page_configuration.section_enable.insert_new_values_in_arguments("")
        self.page_configuration.section_enable.click_in_button_save_configuration()
        self.page_home.click_in_sidebar_button_configurations_page()

        assert ("New Name" in self.page_configuration.section_enable.check_text_returned_in_name_application()
                and "ipconfig" in self.page_configuration.section_enable.check_text_returned_in_cmd_and_arg_application())
