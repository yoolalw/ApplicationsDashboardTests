import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver
from tests.pages.configuration.page_base import PageBase
from tests.pages.configuration.section_enable_apps import SectionEnableApps


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


            # Container log
        self.button_download_logs = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[1]/button')

            # Container geral
        self.button_internal_server = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[1]/div/button[1]')
        self.button_customized_url = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[1]/div/button[2]')

            # Configuration for internal server
        self.input_customized_homepage_url = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/label/input')
        self.button_send_page_archive = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[2]/div[2]/label')
        self.button_preview_with_archive_customized = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[2]/div[2]/button')
        self.button_restart_without_archive = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[2]/div[2]/button[2]')
            # Standard container
        self.checkbox_advanced_resources = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[2]/div[2]/label/input')
        self.input_port_for_remote_connection = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[3]/div[2]/label[1]/input')
        self.checkbox_accept_remote_connection = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[3]/div[2]/label[2]/input')
        self.input_directory = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[2]/input')
        self.button_create = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[2]/button')
        self.container_internal_folder = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[3]/div[2]')
        self.button_auto_start_instance = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[5]/div[2]/button')
        self.container_auto_start_instance = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[5]/div[2]/div/p')
        self.button_import_json_file = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/div/button[1]')
        self.button_download_backup_file = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/div/button[2]')
        self.checkbox_replace_all_instances = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/label/input')
        self.button_save_configurations = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/div/div/button')

        self.count_all_apps = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[1]/p[2]')
        self.count_visible_apps = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[2]/p[2]')
        self.count_disabled_apps = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[3]/p[2]')

            # Container style
        self.button_card_view = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[1]/div/button[1]')
        self.button_list_view = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[1]/div/button[2]')
        self.button_theme_light = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[2]/div/button[1]')
        self.button_theme_dark = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[2]/div/button[2]')
        self.button_color_blue_standard = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[1]')
        self.button_color_blue_ocean = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[2]')
        self.button_color_green = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[3]')
        self.button_color_red_alert = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[4]')
        self.button_color_purple_signal = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[5]')
        self.button_color_orange_energy = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[6]')
        self.button_color_white_clean = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[7]')
        self.button_color_random = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[8]')
        self.button_save_configurations_style_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[4]/div/button')

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

