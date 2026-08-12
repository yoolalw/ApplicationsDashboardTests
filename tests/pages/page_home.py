from time import sleep

import pytest
import allure
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.title = (By.XPATH, '//*[@id="root"]/div/header/div[1]/div/h1')

        self.language_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/button')
        self.alert_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/button[1]')
        self.new_application = (By.XPATH, '//*[@id="root"]/div/header/div[2]/button[2]')

        # These XPATH are for the 'Ping Test Internet' instance. The execution begins with the JSON file.
        self.title_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/h3')
        self.start_button = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[2]/div[2]/button[1]')
        self.config_button = (By.XPATH,
                              '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[2]/div[2]/button[2]')

        self.status_button = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/div/span[2]')

        self.container_languages = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div/button')
        self.pt_language = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div/button[1]')

        # To create new applications !
        self.container_title_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/div/h2')
        self.container_input_name_new_app = (By.XPATH,
                                             '/html/body/div/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[1]/input')
        self.container_input_port_new_app = (By.XPATH,
                                             '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/div/label[1]/input')
        self.container_input_directory_new_app = (By.XPATH,
                                                  '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/div/label[2]/input')
        self.container_input_command_new_app = (By.XPATH,
                                                '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[3]/input')
        self.container_input_arguments_new_app = (By.XPATH,
                                                  '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[4]/input')
        self.container_input_web_link_new_app = (By.XPATH,
                                                 '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[5]/input')
        self.container_button_add_app_new_app = (By.XPATH,
                                                 '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[2]')
        self.container_button_cancel_new_app = (By.XPATH,
                                                '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[1]')

        self.alert_message_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/section/ul/li')

        # To insert new configuration in 'Ping Teste Internet'
        self.config_input_name = (By.XPATH,
                                  '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[1]/input')
        self.config_input_port = (By.XPATH,
                                  '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section/div/div/label[1]/input')
        self.config_input_directory = (By.XPATH,
                                       '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section/div/div/label[2]/input')
        self.config_input_command = (By.XPATH,
                                     '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section/div/label[3]/input')
        self.config_input_arguments = (By.XPATH,
                                       '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section/div/label[4]/input')
        self.config_add_app_button = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[2]')

        self.container_terminal = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/div')

        self.all_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]')

        self.mark_all_read_button = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[1]')
        self.clear_all_button = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[2]')

        self.status_text = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/div/span[2]')

    @allure.step('Verifying fixed elements on the screen')
    def verifying_if_the_elements_are_displayed(self):
        return self.driver.find_element(*self.title).is_displayed() and \
            self.driver.find_element(*self.language_button).is_displayed() and \
            self.driver.find_element(*self.alert_button).is_displayed() and \
            self.driver.find_element(*self.new_application).is_displayed()

    @allure.step('Selecting languages')
    def selecting_language(self):
        self.driver.find_element(*self.language_button).click()
        btns = self.driver.find_elements(*self.container_languages)
        for i in range(len(btns)):
            btns = self.driver.find_elements(*self.container_languages)
            btns[i].click()
            self.driver.find_element(*self.language_button).click()

    @allure.step('Click in container "Ping Teste Internet"')
    def click_in_container(self):
        self.wait.until(ec.visibility_of_element_located(self.all_container)).click()

    @allure.step('Verifying creation of the item "Ping Test Internet" ')
    def container_auto_created_from_json(self):
        return self.wait.until(ec.visibility_of_element_located(self.title_container)) and \
            self.wait.until(ec.visibility_of_element_located(self.status_button)) and \
            self.wait.until(ec.visibility_of_element_located(self.config_button)) and \
            self.wait.until(ec.visibility_of_element_located(self.start_button))

    @allure.step('Clicking in alert button')
    def click_in_alert_button(self):
        self.wait.until(ec.visibility_of_element_located(self.alert_button)).click()

    @allure.step('Clicking in new app button')
    def click_in_new_application(self):
        self.driver.find_element(*self.new_application).click()
        return self.wait.until(ec.visibility_of_element_located(self.container_title_new_app)).is_displayed()

    @allure.step('Verifying if the terminal are displayed')
    def terminal_displayed(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_terminal)).is_displayed()

    @allure.step('Creating new application')
    def creating_new_application(self, input_name, input_port, input_directory, input_cmd, input_arguments):
        self.wait.until(ec.visibility_of_element_located(self.container_input_name_new_app)).send_keys(input_name)
        self.wait.until(ec.visibility_of_element_located(self.container_input_port_new_app)).send_keys(input_port)
        self.wait.until(ec.visibility_of_element_located(self.container_input_directory_new_app)).send_keys(
            input_directory)
        self.wait.until(ec.visibility_of_element_located(self.container_input_command_new_app)).send_keys(input_cmd)
        self.wait.until(ec.visibility_of_element_located(self.container_input_arguments_new_app)).send_keys(
            input_arguments)

    @allure.step('Click in "Add App" (New Application container)')
    def click_in_add_app(self):
        self.wait.until(ec.visibility_of_element_located(self.container_button_add_app_new_app)).click()

    @allure.step('Validate error message - Input Name')
    def verification_message_input_name(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_input_name_new_app)).get_attribute(
            'validationMessage')

    @allure.step('Validate error message - Input Commmand')
    def verification_message_input_cmd(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_input_command_new_app)).get_attribute(
            'validationMessage')

    @allure.step('Click in "Start" button - Ping Teste Internet')
    def starting_application_ping_teste_internet(self):
        self.wait.until(ec.visibility_of_element_located(self.start_button)).click()

    @allure.step('Verifying if the status has been changed')
    def status_application_ping_teste_internet(self):
        return self.wait.until(ec.visibility_of_element_located(self.status_text)).text

    @allure.step('Click in "Configuration" button - Ping Teste Internet')
    def click_in_configuration_button_ping_teste_internet(self):
        self.wait.until(ec.visibility_of_element_located(self.config_button)).click()

    @allure.step('Inserting new configuration on Ping Teste Internet')
    def inserting_new_configuration_to_ping_server_internet(self, name, command, arguments):
        name_input = self.wait.until(ec.visibility_of_element_located(self.config_input_name))
        name_input.clear()
        name_input.send_keys(name)
        cmd_input = self.wait.until(ec.visibility_of_element_located(self.config_input_command))
        cmd_input.clear()
        cmd_input.send_keys(command)

        arg_input = self.wait.until(ec.visibility_of_element_located(self.config_input_arguments))
        arg_input.clear()
        arg_input.send_keys(arguments)

    @allure.step('Click in "Add App" (Configuration container) - Ping Teste Internet')
    def click_to_save_new_configuration(self):
        self.wait.until(ec.visibility_of_element_located(self.config_add_app_button)).click()

    @allure.step('Verifying title from Ping Teste Internet has been changed to -> New Title')
    def title_ping_teste_internet(self):
        return self.wait.until(ec.visibility_of_element_located(self.title_container)).text

    @allure.step('Starting the application')
    def starting_the_error_try_application(self):
        self.wait.until(ec.visibility_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[4]/div[2]/div[2]/button[2]'))).click()

    @allure.step('Verifying error message container displayed')
    def verifying_alert_message_generated(self):
        return self.wait.until(ec.visibility_of_element_located(self.alert_message_container)).is_displayed()

    @allure.step('Mark all alerts read')
    def mark_alerts_read(self):
        self.wait.until(ec.visibility_of_element_located(self.mark_all_read_button)).click()

    @allure.step('Clear all alerts container')
    def click_in_clear_all_button(self):
        self.wait.until(ec.visibility_of_element_located(self.clear_all_button)).click()
