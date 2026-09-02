import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver
from tests.pages.configuration.page_base import PageBase
from tests.pages.configuration.section_enable_apps import SectionEnableApps
from tests.pages.configuration.section_general import SectionGeneral


class PageConfiguration(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.button_refresh_page = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[1]/button')
        # Bar
        self.bar_button_enable_apps = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[1]')
        self.bar_button_logs_system = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[2]')
        self.bar_button_geral = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[3]')
        self.bar_button_style = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[4]')
        self.bar_button_advanced_resources = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[5]')

        self.section_enable = SectionEnableApps(driver)
        self.section_general = SectionGeneral(driver)


            # Container advanced resources
        self.button_enable_ai_chat = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[1]')
        self.button_enable_api_tester = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[4]')
        self.button_enable_tests_and_connectivity = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[4]')
        self.button_enable_mini_server_web = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[4]')
        self.button_enable_scripts = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[5]')
        self.button_enable_central_alerts = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[3]')

            # Ai Chat configuration
        self.select_open_ai_provider = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/div/label[1]/select')
        self.select_options = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/div/label[1]/select/option')
        self.input_model_ai = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/label[1]/input')
        self.input_base_url_customized = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/label[2]/input')
        self.button_save_configurations_adv_resources_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div/button')

