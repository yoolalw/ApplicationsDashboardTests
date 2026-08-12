from idlelib.colorizer import prog_group_name_to_tag
from time import sleep

import allure
import pytest
from pygments.lexers.css import SassLexer
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.page_home import HomePage

from conftest import driver


@allure.title('Tests in Page Home')
@allure.description('The tests will consist the assertions from new created applications')
@pytest.mark.usefixtures('driver')
class TestHomePage:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.home_page = HomePage(self.driver)

    # PDT01
    def test_verifying_if_home_are_running(self):
        assert self.home_page.verifying_if_the_elements_are_displayed()

    # PDT02
    def test_verifying_if_the_auto_container_has_been_created(self):
        assert self.home_page.container_auto_created_from_json()

    # PDT03
    def test_changes_the_language_and_checking_if_all_application_has_been_modified(self):
        self.home_page.selecting_language()
        assert True

    # PDT04
    def test_click_in_new_app_button(self):
        assert self.home_page.click_in_new_application()

    # PDT07 + PDT08
    @pytest.mark.parametrize(
        "name, port, directory, cmd, arguments",
        [
            ('NameApplication', '8020', r"C:\Users\WSC-Convidado\Downloads\api (1).zip", "mvn", 'spring-boot:run'),
            (34284033264782, '2323', "dhaidh ababa ijoifhg sdsif", "mvn", 'spring-boot/run'),
            ('s*@&#(&*@#($&(@*¨(&', '1', r"C:\Users\WSC-Convidado\Downloads\api (1).zip", "mvn",
             'spring-boot:run'),
            ('App_Local_Tefsafast', '9000', r"C:\ryuSa\Ryu\demo\demo", "mvn", 'spring-boot:run'),
        ]
    )
    def test_creating_new_application_with_directory(self, name, port, directory, cmd, arguments):
        self.home_page.click_in_new_application()
        self.home_page.creating_new_application(name, port, directory, cmd, arguments)
        self.home_page.click_in_add_app()

    @pytest.mark.parametrize(
        "name, port, directory, cmd, arguments, expected",
        [
            ("", '1234', "/apps/api.exe", 'npm', 'start run', 'Preencha este campo.'),
            ("name", '1234', "/directory", '', 'start run', 'Preencha este campo.'),
        ]
    )
    def test_verifying_field_null_message(self, name, port, directory, cmd, arguments, expected):
        self.home_page.click_in_new_application()
        self.home_page.creating_new_application(name, port, directory, cmd, arguments)
        self.home_page.click_in_add_app()
        assert expected in self.home_page.verification_message_input_name() or self.home_page.verification_message_input_cmd()

    def test_starting_application_and_verifying_if_status_change(self):
        self.home_page.starting_application_ping_teste_internet()
        assert 'running' in self.home_page.status_application_ping_teste_internet()

    def test_creating_new_configuration_in_application(self):
        self.home_page.click_in_configuration_button_ping_teste_internet()
        self.home_page.inserting_new_configuration_to_ping_server_internet('New name', 'ping','8.8.8.8 -t')
        self.home_page.click_to_save_new_configuration()
        assert 'New name' in self.home_page.title_ping_teste_internet()

        self.home_page.starting_application_ping_teste_internet()
        assert 'running' in self.home_page.status_application_ping_teste_internet()

    def test_verifying_if_terminal_are_running(self):
        self.home_page.starting_application_ping_teste_internet()
        self.home_page.click_in_container()
        return self.home_page.terminal_displayed()