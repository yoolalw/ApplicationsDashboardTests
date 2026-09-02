import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.configuration.page_base import PageBase


class SectionGeneral(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        # Container geral
        self.button_internal_server = (By.XPATH,
                                       '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[1]/div/button[1]')
        self.button_customized_url = (By.XPATH,
                                      '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[1]/div/button[2]')

        # Configuration for internal server
        self.input_customized_homepage_url = (By.XPATH,
                                              '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/label/input')
        self.button_send_page_archive = (By.XPATH,
                                         '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[2]/div[2]/label')
        self.button_preview_with_archive_customized = (By.XPATH,
                                                       '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[2]/div[2]/button')
        self.button_restart_without_archive = (By.XPATH,
                                               '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[1]/div[2]/div[2]/div[2]/button[2]')
        # Standard container
        self.checkbox_advanced_resources = (By.XPATH,
                                            '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[2]/div[2]/label/input')
        self.input_port_for_remote_connection = (By.XPATH,
                                                 '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[3]/div[2]/label[1]/input')
        self.checkbox_accept_remote_connection = (By.XPATH,
                                                  '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[3]/div[2]/label[2]/input')
        self.input_directory = (By.XPATH,
                                '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[2]/input')
        self.button_create = (By.XPATH,
                              '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[2]/button')
        self.container_internal_folder = (By.XPATH,
                                          '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[3]/div[2]')
        self.button_auto_start_instance = (By.XPATH,
                                           '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[5]/div[2]/button')
        self.container_auto_start_instance = (By.XPATH,
                                              '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[5]/div[2]/div/p')
        self.button_import_json_file = (By.XPATH,
                                        '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/div/button[1]')
        self.button_download_backup_file = (By.XPATH,
                                            '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/div/button[2]')
        self.checkbox_replace_all_instances = (By.XPATH,
                                               '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[6]/div[2]/label/input')
        self.button_save_configurations = (By.XPATH,
                                           '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/div/div/button')

        self.count_all_apps = (By.XPATH,
                               '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[1]/p[2]')
        self.count_visible_apps = (By.XPATH,
                                   '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[2]/p[2]')
        self.count_disabled_apps = (By.XPATH,
                                    '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[3]/p[2]')

    # Clicks !
    @allure.step("Click in button to include internao server")
    def click_button_internal_server(self):
        self.click(self.button_internal_server)

    @allure.step("Click in button to customize urç")
    def click_button_customized_url(self):
        self.click(self.button_customized_url)

    @allure.step("Click in button to send page archive")
    def click_button_button_send_page_archive(self):
        self.click(self.button_send_page_archive)

    @allure.step("Click in button to preview with the archive customized")
    def click_button_to_preview_with_archive_customized(self):
        self.click(self.button_preview_with_archive_customized)

    @allure.step("Click in button to restart without archive")
    def click_button_to_restart_without_archive(self):
        self.click(self.button_restart_without_archive)

    @allure.step("Click in button to create")
    def click_button_to_create(self):
        self.click(self.button_create)

    @allure.step("Click button to enable auto start instance")
    def click_button_enable_auto_start(self):
        self.click(self.button_auto_start_instance)

    @allure.step("Click in button to import new json file")
    def click_button_import_json_file(self):
        self.click(self.button_import_json_file)

    @allure.step("Click in button to download backup files")
    def click_button_download_backup_file(self):
        self.click(self.button_download_backup_file)

    @allure.step("Click in button to save all new configuration")
    def click_button_save_configurations(self):
        self.click(self.button_save_configurations)

    # Inputs !
    @allure.step("Inserting new customized homepage url")
    def inserting_customized_url(self, value):
        self.fill(self.input_customized_homepage_url, value)

    @allure.step("Inserting new port for remote connection")
    def inserting_new_port_for_remote_connection(self, value):
        self.fill(self.input_directory, value)

    @allure.step("Inserting new directory")
    def inserting_new_directory(self, value):
        self.fill(self.input_directory, value)


    # CheckBox !
    @allure.step("Checking options in CheckBox -> Advanced Resources")
    def checks_advanced_resources(self):
        self.click(self.checkbox_advanced_resources)

    @allure.step("Checking options in CheckBox -> Accept Remote Connection")
    def checks_accept_remote_connection(self):
        self.click(self.checkbox_accept_remote_connection)

    @allure.step("Checking options in CheckBox -> Replace All Instances")
    def checks_replace_all_instances(self):
        self.click(self.checkbox_replace_all_instances)

    # Texts !
    @allure.step("Verifying all apps count")
    def verifying_all_apps_count(self):
        return self.text(self.count_all_apps)

    @allure.step("Verifying all visible apps count")
    def verifying_all_visible_apps_count(self):
        return self.text(self.count_visible_apps)

    @allure.step("Verifying all disabled apps count")
    def verifying_all_disabled_apps(self):
        return self.text(self.count_disabled_apps)
