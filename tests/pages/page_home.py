from time import sleep

import pytest
import allure
from dotenv import set_key
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec


from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver

class PageHome:
    def __init__(self, driver: WebDriver):
        #start
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.page_title = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[1]/div[1]/h2')

        #language
        self.languages_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/button')
        self.languages_container = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div/button')
        self.language = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div/button[1]')

        #alert
        self.alert_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/button[1]')
        self.alert_title = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[1]/div[1]/h2')
        self.alert_button_mark_all_read = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[1]')
        self.alert_button_clear_all = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[2]')
        self.alert_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/section/div')
        self.alert_message_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/section/ul/li')

        #new app
        self.new_app_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/button[2]')
        self.new_app_title = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/div/h2')
        self.new_app_input_name = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[1]/input')
        self.new_app_input_port = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/div/label[1]/input')
        self.new_app_input_directory = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/div/label[2]/input')
        self.new_app_input_command = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[3]/input')
        self.new_app_input_arguments = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[4]/input')
        self.new_app_input_button_add_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[2]')
        self.new_app_input_button_cancel = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[1]')

        #container ping_teste_internet
        self.container_ping_teste_internet = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article')
        self.container_ping_teste_internet_title = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article/div[1]/h3')
        self.container_ping_teste_internet_status = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article/div[1]/div/span[2]')
        self.container_ping_teste_internet_button_start = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article/div[2]/div[2]/button[1]')
        self.container_ping_teste_internet_button_config = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article/div[2]/div[2]/button[2]')

        #container created
        self.container_created = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[2]')
        self.container_created_title = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[2]/div[1]/h3')
        self.container_created_status = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[2]/div[1]/div/span[2]')
        self.container_created_button_start = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[2]/div[2]/div[2]/button[2]')

        self.container_created_button_config = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[2]/div[2]/div[2]/button[3]')

        # container for negative tests
        self.container_created_for_generate_alert = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[3]')
        self.container_created_for_generate_alert_title = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[3]/div[1]/h3')
        self.container_created_for_generate_alert_status = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[3]/div[1]/div/span[2]')
        self.container_created_for_generate_alert_button_start = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[3]/div[2]/div[2]/button[2]')
        self.container_created_for_generate_alert_button_config = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[3]/div[2]/div[2]/button[3]')

        # !! >> sidebar
        self.sidebar_home_button = (By.XPATH, '//*[@id="root"]/div/main/aside/div[1]/button[1]')
        self.sidebar_homepage_button = (By.XPATH, '//*[@id="root"]/div/main/aside/div[1]/button[2]')
        self.sidebar_aichat_button = (By.XPATH, '//*[@id="root"]/div/main/aside/div[1]/button[3]')
        self.sidebar_patchfiles_button = (By.XPATH, '//*[@id="root"]/div/main/aside/div[1]/button[4]')
        self.sidebar_configurations_button = (By.XPATH, '//*[@id="root"]/div/main/aside/div[2]/button[1]')
        self.sidebar_about_button = (By.XPATH, '//*[@id="root"]/div/main/aside/div[2]/button[2]')



    # sidebar clicks
    @allure.step("Click in SideBar button -> Home page")
    def click_in_sidebar_button_home_page(self):
        self.wait.until(ec.element_to_be_clickable(self.sidebar_home_button)).click()

    @allure.step("Click in SideBar button -> HomePage page")
    def click_in_sidebar_button_homepage_page(self):
        self.wait.until(ec.element_to_be_clickable(self.sidebar_homepage_button)).click()

    @allure.step("Click in SideBar button -> AIChat page")
    def click_in_sidebar_button_ai_chat_page(self):
        self.wait.until(ec.element_to_be_clickable(self.sidebar_aichat_button)).click()

    @allure.step("Click in SideBar button -> PatchFiles page")
    def click_in_sidebar_button_patch_files_page(self):
        self.wait.until(ec.element_to_be_clickable(self.sidebar_patchfiles_button)).click()

    @allure.step("Click in SideBar button -> Configurations page")
    def click_in_sidebar_button_configurations_page(self):
        self.wait.until(ec.element_to_be_clickable(self.sidebar_configurations_button)).click()

    @allure.step("Click in SideBar button -> About page")
    def click_in_sidebar_button_home_page(self):
        self.wait.until(ec.element_to_be_clickable(self.sidebar_about_button)).click()

    #displayed elements
    @allure.step("Verifying if the elements are displayed in Home Page")
    def verifying_elements_displayed_in_home(self):
        return self.wait.until(ec.visibility_of_element_located(self.page_title)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.languages_button)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.alert_button)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_button)).is_displayed()

    @allure.step("Verifying if the 'Ping Teste Internet' has been created")
    def verifying_if_ping_teste_internet_application_has_been_displayed(self):
        return self.wait.until(ec.text_to_be_present_in_element(self.container_ping_teste_internet_title, 'Ping Teste Internet'))

    @allure.step("Checking all elements in container displayed - Ping Teste Internet")
    def verifying_if_the_container_has_been_created(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_created)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.container_created_title)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.container_created_status)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.container_created_button_config)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.container_created_button_start)).is_displayed()

    @allure.step("Verifying alert message displayed")
    def verifying_if_the_alert_has_been_generated(self):
        return self.wait.until(ec.visibility_of_element_located(self.alert_message_container)).is_displayed()

    #click elements
    @allure.step("Click in language -> Portuguese")
    def click_to_change_language_for_portuguese(self):
        self.wait.until(ec.visibility_of_element_located(self.language)).click()

    @allure.step("Click in configurations from the created container")
    def click_configurations_from_the_container_created(self):
        self.wait.until(ec.visibility_of_element_located(self.container_created_button_config)).click()

    @allure.step("Click in button to change website language ")
    def click_in_languages_button(self):
        self.wait.until(ec.visibility_of_element_located(self.languages_button)).click()

    @allure.step("Click in button to mark all alerts read")
    def click_to_mark_all_alerts_read(self):
        self.wait.until(ec.visibility_of_element_located(self.alert_button_mark_all_read)).click()

    @allure.step("Click in button to clear all alert container")
    def click_to_clear_all_container_from_alerts(self):
        self.wait.until(ec.visibility_of_element_located(self.alert_button_clear_all)).click()

    @allure.step("Click in button to start the created application")
    def click_on_start_the_application_created(self):
        self.wait.until(ec.element_to_be_clickable(self.container_created_button_start)).click()

    @allure.step("Click in button to start the application with errors")
    def click_on_start_button_for_application_with_wrong_application(self):
        self.wait.until(ec.visibility_of_element_located(self.container_created_for_generate_alert_button_start)).click()

    @allure.step("Click in 'New App+' button")
    def click_on_new_app_button(self):
        self.wait.until(ec.visibility_of_element_located(self.new_app_button)).click()
        return self.wait.until(ec.visibility_of_element_located(self.new_app_title)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_input_name)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_input_port)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_input_directory)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_input_command)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_input_arguments)) .is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_input_button_add_app)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_input_button_cancel)).is_displayed()
    @allure.step("Click in 'Add App' in 'New App+' container")
    def click_in_new_app_add_app_button(self):
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_button_add_app)).click()

    @allure.step("Click in 'Alert' button")
    def click_in_alert_icon(self):
        self.wait.until(ec.visibility_of_element_located(self.alert_button)).click()

    @allure.step("Click in 'Cancel' in 'New App+' container")
    def click_in_new_app_cancel_button(self):
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_button_cancel)).click()

    @allure.step("Click in start button after the changes")
    def click_in_start_application_after_changes(self):
        for attempt in range(3):
            try:
                self.wait.until(
                    ec.element_to_be_clickable(
                        self.container_created_button_start
                    )
                ).click()
                return
            except StaleElementReferenceException:
                if attempt == 2:
                    raise
    #texts
    @allure.step("Verifying the text returned from title in 'Alert' container")
    def verifying_text_from_alerts_container(self):
        return self.wait.until(ec.visibility_of_element_located(self.alert_container)).text

    @allure.step("Verifying the status from the created container")
    def verifying_status_from_created_container(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_created_status)).text

    @allure.step("Verifying status with error configuration container")
    def verifying_status_from_container_with_error_configuration(self):
        return self.wait.until(ec.text_to_be_present_in_element(self.container_created_for_generate_alert_status, 'failed'))

    #inserting / alter elements
    @allure.step("Change the configuration from the new container created")
    def changes_configuration_from_the_container_created(self, input_name, input_port, input_directory, input_command, input_arguments):
        input_new_name = self.wait.until(ec.visibility_of_element_located(self.new_app_input_name))
        input_new_name.clear()
        input_new_name.send_keys(input_name)

        input_new_port = self.wait.until(ec.visibility_of_element_located(self.new_app_input_port))
        input_new_port.clear()
        input_new_port.send_keys(input_port)

        input_new_directory = self.wait.until(ec.visibility_of_element_located(self.new_app_input_directory))
        input_new_directory.clear()
        input_new_directory.send_keys(input_directory)

        input_new_command = self.wait.until(ec.visibility_of_element_located(self.new_app_input_command))
        input_new_command.clear()
        input_new_command.send_keys(input_command)

        input_new_arguments = self.wait.until(ec.visibility_of_element_located(self.new_app_input_arguments))
        input_new_arguments.clear()
        input_new_arguments.send_keys(input_arguments)

    @allure.step('Creating new application')
    def creating_new_application(self, input_name, input_port, input_directory, input_command, input_arguments):
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_name)).send_keys(input_name)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_port)).send_keys(input_port)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_directory)).send_keys(input_directory)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_command)).send_keys(input_command)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_arguments)).send_keys(input_arguments)

    @allure.step("Switch the system language")
    def switch_system_language(self):
        self.driver.find_element(*self.languages_button).click()
        container = self.driver.find_elements(*self.languages_container)

        for i in range(len(container)):
            container = self.driver.find_elements(*self.languages_container)
            container[i].click()
            self.driver.find_element(*self.languages_button).click()
