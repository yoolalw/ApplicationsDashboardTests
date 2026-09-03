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
        self.configuration = PageConfiguration(self.driver)

    # Tests -> Enabled/Disabled Apps Section!
    @allure.id("CED01")
    @allure.title("Verifying if the container exists")
    def test_verifying_if_the_container_are_displayed(self):
        assert self.configuration.section_enable.verifying_displayed_container()

    @allure.id("CS03")
    @allure.title("Click in button to change the color to 'Ocean Blue' ")
    def test_change_the_color_of_system_to_ocean_blue(self):
        self.configuration.click_in_bar_button_style()
        self.configuration.section_style.click_button_color_blue_ocean()
        assert '37, 99, 235' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()

    @allure.id("CS04")
    @allure.title("Click in button to change the color to 'Green' ")
    def test_change_the_color_of_system_to_green(self):
        self.configuration.click_in_bar_button_style()
        self.configuration.section_style.click_button_color_green()
        assert '22, 163, 74' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()

    @allure.id("CS05")
    @allure.title("Click in button to change the color to 'Red Alert' ")
    def test_change_the_color_of_system_to_red_alert(self):
        self.configuration.click_in_bar_button_style()
        self.configuration.section_style.click_button_color_red_alert()
        assert '220, 38, 38' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()

    @allure.id("CS06")
    @allure.title("Click in button to change the color to 'Purple Signal' ")
    def test_change_the_color_of_system_to_purple_signal(self):
        self.configuration.click_in_bar_button_style()
        self.configuration.section_style.click_button_color_purple_signal()
        assert '147, 51, 234' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()


    @allure.id("CS07")
    @allure.title("Click in button to change the color to 'Energy Orange'")
    def test_change_the_color_of_system_to_orange_energy(self):
        self.configuration.click_in_bar_button_style()
        self.configuration.section_style.click_button_color_orange_energy()
        assert '249, 115, 22' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()

    @allure.id("CS08")
    @allure.title("Click in button to change the color to '' ")
    def test_change_the_color_of_system_to(self):
        self.configuration.click_in_bar_button_style()
        self.configuration.section_style.click_button_color_purple_signal()
        assert '147, 51, 234' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()

    @allure.id("CS09")
    @allure.title("Click in button to change the color to 'Clean White' ")
    def test_change_the_color_of_system_to_green(self):
        self.configuration.click_in_bar_button_style()
        self.configuration.section_style.click_button_color_purple_signal()
        assert '255, 255, 255' in self.configuration.section_style.return_the_color_from_circle()
        self.configuration.section_style.click_button_to_save_configurations()


