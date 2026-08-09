import pytest
import allure
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.title = (By.XPATH, '//*[@id="root"]/div/header/div[1]/div/h1' )

        self.language_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/div/button')
        self.alert_button = (By.XPATH, '//*[@id="root"]/div/header/div[2]/button[1]')
        self.new_application = (By.XPATH, '//*[@id="root"]/div/header/div[2]/button[2]')

        # These XPATH are for the 'Ping Test Internet' instance. The execution begins with the JSON file.
        self.title_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/h3')
        self.status_container = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/div/span[2]')
        self.status_container_color = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[1]/div/span[1]')
        self.start_button = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[2]/div[2]/button[1]')
        self.config_button = (By.XPATH, '//*[@id="root"]/div/main/section/div/div[2]/article[1]/div[2]/div[2]/button[2]')

    @allure.step('Verifying fixed elements on the screen')
    def verifying_if_the_elements_are_displayed(self):
        return self.driver.find_element(self.title).is_displayed() and \
            self.driver.find_element(self.language_button) and \
            self.driver.find_element(self.alert_button) and \
            self.driver.find_element(self.new_application)

    @allure.step('Verifying creation of the item "Ping Test Internet" ')
    def container_created_from_json(self):
        return self.wait.until(ec.visibility_of_element_located(self.title_container)) and \
            self.wait.until(ec.visibility_of_element_located(self.status_container)) and \
            self.wait.until(ec.visibility_of_element_located(self.status_container_color)) and \
            self.wait.until(ec.visibility_of_element_located(self.config_button)) and \
            self.wait.until(ec.visibility_of_element_located(self.start_button))

    @allure.step('Clicking in language button')
    def clicking_in_language_button(self):
        self.driver.find_element(self.language_button).click()

    @allure.step('Clicking in alert button')
    def clicking_in_alert_button(self):
        self.driver.find_element(self.alert_button).click()

    @allure.step('Clicking in new app button')
    def clicking_in_new_application(self):
        self.driver.find_element(self.new_application).click()


