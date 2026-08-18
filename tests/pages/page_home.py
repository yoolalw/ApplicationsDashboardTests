import pytest
import allure
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
        self.languages_container = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div')
        self.language = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div/button[1]')
        #alert
        self.alert_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/button[1]')
        self.alert_title = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[1]/div[1]/h2')
        self.alert_button_mark_all_read = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[1]')
        self.alert_button_clear_all = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/button[2]')
        self.alert_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/section/div')
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

    #displayed elements

    def verifying_elements_displayed_in_home(self):
        return self.wait.until(ec.visibility_of_element_located(self.page_title)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.languages_button)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.alert_button)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.new_app_button)).is_displayed()

    def verifying_if_ping_teste_internet_application_has_been_displayed(self):
        return self.wait.until(ec.text_to_be_present_in_element(self.container_ping_teste_internet_title, 'Ping Teste Internet'))

    #click elements
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

    def click_in_new_app_add_app_button(self):
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_button_add_app)).click()

    def click_in_new_app_cancel_button(self):
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_button_cancel)).click()



    #inserting / alter elements
    def creating_new_application(self, input_name, input_port, input_directory, input_command, input_arguments):
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_name)).send_keys(input_name)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_port)).send_keys(input_port)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_directory)).send_keys(input_directory)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_command)).send_keys(input_command)
        self.wait.until(ec.visibility_of_element_located(self.new_app_input_arguments)).send_keys(input_arguments)


    def switch_system_language(self):
        self.wait.until(ec.element_to_be_clickable(self.languages_button)).click()
        all_languages = self.wait.until(ec.visibility_of_element_located(self.language))
        for i in range(len(all_languages)):
            specify_language = self.wait.until(ec.visibility_of_element_located(self.language))
            actual_language = specify_language[i]
            actual_language.click()
