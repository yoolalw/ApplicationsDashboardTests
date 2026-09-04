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
class TestsPageConfigurationSectionStyle:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.page_home = PageHome(self.driver)
        self.page_home.click_in_sidebar_button_configurations_page()
        self.configuration = PageConfiguration(self.driver)
        self.configuration.click_in_bar_button_style()

        # Tests -> Style Section !
    @allure.id("CS01")
    @allure.title("Click button to change the format of the card and verifying if has been changed (To Card Format)")
    def test_change_card_format_to_card(self):
        self.configuration.section_style.click_button_card_view()
        self.configuration.section_style.click_button_to_save_configurations()
        self.page_home.click_in_sidebar_button_home_page()
        width_container = self.page_home.return_width_from_ping_teste_internet()
        height_container = self.page_home.return_height_from_ping_teste_internet()
        assert width_container >= height_container

    @allure.id("CS02")
    @allure.title("Click button to change the format of the card and verifying if has been changed (To List Format)")
    def test_change_card_format_to_list(self):
        self.configuration.section_style.click_button_list_view()
        self.configuration.section_style.click_button_to_save_configurations()
        self.page_home.click_in_sidebar_button_home_page()
        width_container = self.page_home.return_width_from_ping_teste_internet()
        height_container = self.page_home.return_height_from_ping_teste_internet()
        assert width_container > height_container

    @allure.id("CS03")
    @allure.title("Click in button to change the color to 'Ocean Blue' ")
    def test_change_the_color_of_system_to_ocean_blue(self):
        self.configuration.section_style.click_button_color_blue_ocean()
        assert '37, 99, 235' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Passed

    @allure.id("CS04")
    @allure.title("Click in button to change the color to 'Green' ")
    def test_change_the_color_of_system_to_green(self):
        self.configuration.section_style.click_button_color_green()
        assert '22, 163, 74' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Failed -> Wrong RGB
    # Passed

    @allure.id("CS05")
    @allure.title("Click in button to change the color to 'Red Alert' ")
    def test_change_the_color_of_system_to_red_alert(self):
        self.configuration.section_style.click_button_color_red_alert()
        assert '220, 38, 38' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Passed

    @allure.id("CS06")
    @allure.title("Click in button to change the color to 'Purple Signal' ")
    def test_change_the_color_of_system_to_purple_signal(self):
        self.configuration.section_style.click_button_color_purple_signal()
        assert '147, 51, 234' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Passed

    @allure.id("CS07")
    @allure.title("Click in button to change the color to 'Energy Orange'")
    def test_change_the_color_of_system_to_orange_energy(self):
        self.configuration.section_style.click_button_color_orange_energy()
        assert '249, 115, 22' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Passed

    @allure.id("CS08")
    @allure.title("Click in button to change the color to 'Default Blue' ")
    def test_change_the_color_of_system_to_default_blue(self):
        self.configuration.section_style.click_button_color_blue_standard()
        assert '0, 157, 234' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Passed

    @allure.id("CS09")
    @allure.title("Click in button to change the color to 'Clean White' ")
    def test_change_the_color_of_system_to_white_clean(self):
        self.configuration.section_style.click_button_color_white_clean()
        assert '255, 255, 255' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Failed -> Fixed: Function wrong being called (Click in Purple -> Click in White)
    # Passed

    @allure.id("CS10")
    @allure.title("Click in button to change the color to '#03fcf8'")
    def test_change_the_color_to_customized(self):
        self.configuration.section_style.click_button_color_random()
        self.configuration.section_style.inserting_values_in_hex_field("#03fcf8")
        assert '3, 252, 248' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()
    # Passed

    @allure.id("CS11")
    @allure.title("Click in button 'Save Settings' and verifying the success message")
    def test_click_and_save_the_new_configuration_style_and_checking_the_message_returned(self):
        self.configuration.section_style.click_button_to_save_configurations()
        assert 'Settings saved' in self.configuration.section_style.verifying_message_after_save_the_settings()