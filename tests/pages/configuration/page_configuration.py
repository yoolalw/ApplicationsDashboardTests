import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver
from tests.pages.configuration.page_base import PageBase
from tests.pages.configuration.section_advanced_resources import SectionAdvancedResources
from tests.pages.configuration.section_enable_apps import SectionEnableApps
from tests.pages.configuration.section_general import SectionGeneral
from tests.pages.configuration.section_style import SectionStyle


class PageConfiguration(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.button_refresh_page = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[1]/button')
        # Bar
        self.bar_button_enable_apps = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[1]')
        self.bar_button_logs_system = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[2]')
        self.bar_button_general = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[3]')
        self.bar_button_style = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[4]')
        self.bar_button_advanced_resources = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[5]')

        self.section_enable = SectionEnableApps(driver)
        self.section_general = SectionGeneral(driver)
        self.section_style = SectionStyle(driver)
        self.section_section_advanced_resources = SectionAdvancedResources(driver)



    # Click !
    @allure.step("Click in button on bar to show enabled apps")
    def click_in_bar_button_show_enabled_apps(self):
        self.click(self.click_in_bar_button_show_enabled_apps)

    @allure.step("Click in button on bar to show logs from system")
    def click_in_bar_button_logs_system(self):
        self.click(self.bar_button_logs_system)

    @allure.step("Click in button on bar to show general")
    def click_in_bar_button_general(self):
        self.click(self.bar_button_general)

    @allure.step("Click in button on bar to show style options")
    def click_in_bar_button_style(self):
        self.click(self.bar_button_style)

    @allure.step("Click in button on bar to show advanced resources")
    def click_in_bar_button_advanced_resources(self):
        self.click(self.bar_button_advanced_resources)

