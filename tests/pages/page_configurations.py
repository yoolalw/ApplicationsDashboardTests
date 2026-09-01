import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver


class PageConfiguration:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.button_refresh_page = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[1]/button')

        # Bar
        self.bar_button_enable_apps = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[1]')
        self.bar_button_logs_system = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[2]')
        self.bar_button_geral = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[3]')
        self.bar_button_style = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[4]')
        self.bar_button_advanced_resources = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[5]')

        # Principal container
        self.container_principal = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]')

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
        self.input_port_for_remoute_conection = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[3]/div[2]/label[1]/input')
        self.checkbox_accept_remoute_connection = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[3]/div[2]/label[2]/input')
        self.input_directory = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[2]/input')
        self.button_create = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[2]/button')
        self.container_internal_folder = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[3]/div[2]')
        self.button_auto_start_instance = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[5]/div[2]/button')
        self.container_auto_start_instance = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[5]/div[2]/div/p')
        self.button_import_json_file = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/div/button[1]')
        self.button_download_backup_file = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/div/button[2]')
        self.checkbox_replace_all_instances = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/label/input')
        self.button_save_configurations = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/div/div/button')

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

