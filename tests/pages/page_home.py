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
        self.status_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/div/span[2]')
        self.status_container_color = (By.XPATH,
                                       '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/div/span[1]')
        self.start_button = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[2]/div[2]/button[1]')
        self.config_button = (By.XPATH,
                              '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[2]/div[2]/button[2]')
        self.container_languages = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div/button')
        self.pt_language = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/div/button[1]')

        self.container_title_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/div/h2')
        self.container_input_name_new_app = (By.XPATH, '/html/body/div/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[1]/input')
        self.container_input_port_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/div/label[1]/input')
        self.container_input_directory_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/div/label[2]/input')
        self.container_input_command_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[3]/input')
        self.container_input_arguments_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[4]/input')
        self.container_input_web_link_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section[1]/div/label[5]/input')
        self.container_button_add_app_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[2]')
        self.container_button_cancel_new_app = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[1]')

    @allure.step('Verifying fixed elements on the screen')
    def verifying_if_the_elements_are_displayed(self):
        return self.driver.find_element(*self.title).is_displayed() and \
            self.driver.find_element(*self.language_button).is_displayed() and \
            self.driver.find_element(*self.alert_button).is_displayed() and \
            self.driver.find_element(*self.new_application).is_displayed()

    @allure.step('Selecting languages')
    def selecting_language(self):
        self.driver.find_element(*self.language_button).click()
        sleep(1)
        btns = self.driver.find_elements(*self.container_languages)
        sleep(1)
        for i in range(len(btns)):
            btns = self.driver.find_elements(*self.container_languages)
            btns[i].click()
            self.driver.find_element(*self.language_button).click()
            sleep(2)

    @allure.step('Verifying creation of the item "Ping Test Internet" ')
    def container_auto_created_from_json(self):
        return self.wait.until(ec.visibility_of_element_located(self.title_container)) and \
            self.wait.until(ec.visibility_of_element_located(self.status_container)) and \
            self.wait.until(ec.visibility_of_element_located(self.status_container_color)) and \
            self.wait.until(ec.visibility_of_element_located(self.config_button)) and \
            self.wait.until(ec.visibility_of_element_located(self.start_button))

    @allure.step('Clicking in alert button')
    def clicking_in_alert_button(self):
        self.driver.find_element(*self.alert_button).click()

    @allure.step('Clicking in new app button')
    def clicking_in_new_application(self):
        self.driver.find_element(*self.new_application).click()
        return self.wait.until(ec.visibility_of_element_located(self.container_title_new_app)).is_displayed()

    def creating_application_with_web_link(self, input_name, input_port, input_web_link):
        self.wait.until(ec.visibility_of_element_located(self.container_input_name_new_app)).send_keys(input_name)
        self.wait.until(ec.visibility_of_element_located(self.container_input_port_new_app)).send_keys(input_port)
        self.wait.until(ec.visibility_of_element_located(self.container_input_web_link_new_app)).send_keys(input_web_link)

    def clicking_in_add_app(self):
        self.wait.until(ec.visibility_of_element_located(self.container_button_add_app_new_app)).click()


