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
    @allure.story("Click to change status -> From Enabled to Disabled")
    def test_clickdsada_to_change_status_to_disabled(self):
        self.page_configuration.section_enable.click_in_button_disable()
        assert self.page_configuration.section_enable.check_if_text_is_equal_the_expect("Disabled")


