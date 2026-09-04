from time import sleep

import allure
import pyautogui
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
@allure.epic("Tests in Section General System!")
@pytest.mark.usefixtures("driver")
class TestsPageConfigurationSectionGeneral:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.page_home = PageHome(self.driver)
        self.page_home.click_in_sidebar_button_configurations_page()
        self.configuration = PageConfiguration(self.driver)
        self.configuration.click_in_bar_button_general()

        # Tests -> General Section !

    pyautogui.PAUSE = 0.5

    @allure.id("CG01")
    @allure.title("Click to open the 'Internal Server' and verifying if the 'HomePage Url' has been disabled")
    def test_click_to_open_the_internal_server_and_verifying_if_the_url_field_has_been_disabled(self):
        self.configuration.section_general.click_button_internal_server()
        assert not self.configuration.section_general.verifying_if_the_url_field_has_been_enabled()

    @allure.id("CG02")
    @allure.title("Click to 'Upload Page' button and send one file with contains type HTML")
    def test_send_file_in_upload_button(self):
        window_actual = self.driver.current_window_handle

        self.configuration.section_general.click_button_internal_server()
        self.configuration.section_general.click_button_button_send_page_archive()
        while "Abrir" not in pyautogui.getActiveWindowTitle():
            pass
        pyautogui.write(r"C:\Users\WSC-Convidado\Downloads\Teste Funcional - FASE 1 (2).html")
        pyautogui.press("enter")
        self.page_home.click_in_sidebar_button_configurations_page()
        self.configuration.click_in_bar_button_general()
        self.configuration.section_general.click_button_internal_server()
        self.configuration.section_general.click_button_to_preview_with_archive_customized()
        self.wait.until(expected_conditions.new_window_is_opened([window_actual]))
        for window in self.driver.window_handles:
            if window != window_actual:
                self.driver.switch_to.window(window)
                break
        assert self.wait.until(expected_conditions.url_contains('/internal-homepage'))

    # Passed

    @allure.id("CG03")
    @allure.title(
        "Click in 'Reset to default' and verifying if the title in /internal-homepage looks like the standard ")
    def test_reset_the_customized_homepage_internal(self):
        self.configuration.section_general.click_button_internal_server()
        self.configuration.section_general.click_button_to_restart_without_archive()
        self.page_home.click_in_sidebar_button_configurations_page()
        self.page_home.click_in_sidebar_button_configurations_page()
        self.configuration.click_in_bar_button_general()
        self.configuration.section_general.click_button_internal_server()
        self.configuration.section_general.click_button_to_preview_with_archive_customized()
        assert 'Applications Dashboard' in self.driver.title

    # Passed

    @allure.id("CG04")
    @allure.title("Click in 'Custom URL' and check if the field to input customs URLs has been enabled")
    def test_click_in_custom_url_and_verifying_if_the_field_has_been_enabled(self):
        self.configuration.section_general.click_button_customized_url()
        assert self.configuration.section_general.verifying_if_the_url_field_has_been_enabled()

    # Passed

    @allure.id("CG05")
    @allure.title("Inserting new URL in the field enabled")
    def test_inserting_new_url_in_field_enabled(self):
        window_actual = self.driver.current_window_handle
        self.configuration.section_general.click_button_customized_url()
        self.configuration.section_general.inserting_customized_url("https://www.google.com/?zx=1788543545750")
        self.configuration.section_general.click_button_save_configurations()
        self.page_home.click_in_sidebar_button_homepage_page()
        for window in self.driver.window_handles:
            if window != window_actual:
                self.wait.until(expected_conditions.new_window_is_opened([window_actual]))
                self.driver.switch_to.window(window)
                break
        assert self.wait.until(expected_conditions.url_contains('https://www.google.com/?zx=1788543545750'))

    @allure.id("CGH06")
    @allure.title("Disable the options 'Enable advanced features' and verifying if the elements has been not visible")
    def test_disable_the_options_advanced_features(self):
        self.configuration.section_general.checks_advanced_resources()
        self.configuration.section_general.click_button_save_configurations()
        assert self.page_home.verifying_if_the_element_ai_chat_are_displayed() and \
               self.configuration.verifying_if_the_element_bar_advanced_features_are_displayed()

    # Passed

    @allure.id("CG07")
    @allure.title("Inserting value to port container and verifying changes in url from page")
    def test_inserting_new_values_and_verifying_changes_in_url_from_page(self):
        self.configuration.section_general.inserting_new_port_for_remote_connection(4000)
        self.configuration.section_general.checks_accept_remote_connection()
        self.configuration.section_general.click_button_save_configurations()
        assert 'Settings saved' in self.configuration.section_general.verifying_message_returned()
        self.configuration.section_general.inserting_new_port_for_remote_connection(3000)
        self.configuration.section_general.click_button_save_configurations()

    @allure.id("CG08")
    @allure.title("Adding new SubFolder at field, verify insertions and click to button 'Create'")
    def test_add_new_subfolder_verify_inserts_and_create(self):
        new_folder = r"C:\Users\WSC-Convidado\Documents\Web\ApplicationsDashboard\FolderToTests"
        self.configuration.section_general.inserting_new_directory(new_folder)
        self.configuration.section_general.click_button_to_create()
        print(self.configuration.section_general.verifying_if_the_container_has_been_filled())
        assert self.configuration.section_general.verifying_if_the_container_has_been_filled() > 0
        assert 'C_-Users-WSC-Convidado-Documents-Web-ApplicationsDashboard-FolderToTests' in self.configuration.section_general.verifying_if_the_container_values_inside()

    # Passed

    @allure.id("CG09")
    @allure.title("Verifying if the modal has been displayed on screen after click in 'Select Instances'")
    def test_verifying_if_the_modal_has_been_displayed(self):
        self.configuration.section_general.click_button_enable_auto_start()
        assert self.configuration.section_general.displayed_modal_on_screen()

    @allure.id("CG10")
    @allure.title("Trying to enable the first instance with Auto Start feature")
    def test_enable_auto_start_in_instance_from_the_modal(self):
        self.configuration.section_general.click_button_enable_auto_start()
        assert self.configuration.section_general.displayed_modal_on_screen() and \
               'Ping Teste Internet' in self.configuration.section_general.verifying_instance_name_on_modal()
        self.configuration.section_general.check_instance_autostart()
        self.configuration.section_general.click_button_to_save_instances_with_auto_save()

    # Passed

    @allure.id("CG11")
    @allure.title("Click in import JSON and import one array to system")
    def test_import_json_file_to_system(self):
        pass

    @allure.id("CG12")
    @allure.title("Click in button 'Download Backup' and realize backup from the data of system")
    def test_doing_backup_in_system(self):
        pass

# ------------------------------------------------------------------------------------------

@allure.parent_suite("Web Tests -> Applications Dashboard")
@allure.suite("Interface Tests in Configuration Page")
@allure.epic("Tests in Section Style System!")
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
