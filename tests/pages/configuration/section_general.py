import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions

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
        self.container_directory = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[3]/div[2]')
        self.container_directory_folder = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/form/section[4]/div[2]/div[3]/div[2]/span')


        self.count_all_apps = (By.XPATH,
                               '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[1]/p[2]')
        self.count_visible_apps = (By.XPATH,
                                   '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[2]/p[2]')
        self.count_disabled_apps = (By.XPATH,
                                    '//*[@id="root"]/div/main/section/div/div/div[3]/div/aside/section[1]/div[2]/div[3]/p[2]')

        self.modal_instances = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[4]/div')
        self.modal_instances_name = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[4]/div/div[2]/ul/li/label/span')
        self.modal_instances_checkbox = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[4]/div/div[2]/ul/li/label/input')
        self.modal_instances_button_save = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[4]/div/div[3]/button[2]')

        self.message_success = (By.XPATH, '//span[contains(text(), "Settings saved")]')

    # Clicks
    @allure.step("Click in button to include internal server")
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

    @allure.step("Click to save the modal with instances needed to auto start")
    def click_button_to_save_instances_with_auto_save(self):
        self.click(self.modal_instances_button_save)

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
    @allure.step("Checking instance to enable Auto Start")
    def check_instance_autostart(self):
        self.click(self.modal_instances_checkbox)

    @allure.step("Checking options in CheckBox -> Advanced Resources")
    def checks_advanced_resources(self):
        self.click(self.checkbox_advanced_resources)

    @allure.step("Checking options in CheckBox -> Accept Remote Connection")
    def checks_accept_remote_connection(self):
        self.click(self.checkbox_accept_remote_connection)

    @allure.step("Checking options in CheckBox -> Replace All Instances")
    def checks_replace_all_instances(self):
        self.click(self.checkbox_replace_all_instances)

    # Displayed items in container 'Folder'
    @allure.step("Verifying length from the container has contain directories")
    def verifying_if_the_container_has_been_filled(self):
        return len(self.container_directory)

    @allure.step("Verifying text from the container has contain directories")
    def verifying_if_the_container_values_inside(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.container_directory_folder)).text



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

    @allure.step("Verifying message returned after click in buttom to save all settings")
    def verifying_message_returned(self):
        return self.text(self.message_success)
    @allure.step("Verifying if the name of instance on modal")
    def verifying_instance_name_on_modal(self):
        return self.text(self.modal_instances_name)

    # Displayed !
    @allure.step("Verifying if the modal has been present on screen")
    def displayed_modal_on_screen(self):
        return self.displayed(self.modal_instances)

    # Attributes !
    @allure.step("Verifying if the URL field has been enabled")
    def verifying_if_the_url_field_has_been_enabled(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.input_customized_homepage_url)).is_enabled()