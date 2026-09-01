import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class PageHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # 1 - Ping Teste Internet
        self.container_without_web_link = (By.XPATH, '/html/body/main/section[2]/article')
        self.container_without_web_link_status = (By.XPATH, '/html/body/main/section[2]/article/div[2]/span[1]')
        self.container_without_web_link_message = (By.XPATH, '/html/body/main/section[2]/article[1]/div[2]/span[2]')

        # 2 - applicationWithTheWebLink
        self.container_with_web_link = (By.XPATH, '/html/body/main/section[2]/article[2]')
        self.container_with_web_link_status = (By.XPATH, '/html/body/main/section[2]/article[2]/div[2]/span[1]')
        self.container_with_web_link_open_button = (By.XPATH, '/html/body/main/section[2]/article[2]/div[2]/a')

        self.button_open_control_panel = (By.XPATH, '/html/body/header/a')

    # Displayed elements
    @allure.step("Verifying if the containers are displayed")
    def verifying_if_the_containers_has_been_present(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_without_web_link)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.container_with_web_link)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.button_open_control_panel)).is_displayed()

    @allure.step("Verifying all elements in 'Container Without Web Link'")
    def verifying_elements_into_container_without_web_link(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_without_web_link_status)).is_displayed()

    @allure.step("Verifying all elements in 'Container With Web Link'")
    def verifying_elements_into_container_with_web_link(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.container_with_web_link_open_button)).is_displayed() and \
            self.wait.until(ec.visibility_of_element_located(self.container_without_web_link_status)).is_displayed()

    # Checking texts in page
    @allure.step("Checking text -> Message generated if the container dont have the web link present")
    def checking_text_returned_from_container_without_web_link(self):
        return self.wait.until(ec.visibility_of_element_located(self.container_without_web_link_message)).text

    # Click on buttons
    @allure.step("Click in 'Open Control Panel'")
    def click_in_button_open_control_panel(self):
        self.wait.until(ec.element_to_be_clickable(self.button_open_control_panel)).click()

    @allure.step("Click in 'Open -> applicationWithWebLink'")
    def click_in_button_open_application_with_web_link(self):
        running = self.wait.until(ec.text_to_be_present_in_element(self.container_with_web_link_status, 'Running'))
        if running:
            self.wait.until(ec.element_to_be_clickable(self.container_with_web_link_open_button)).click()

    @allure.step("Verifying if the status has been changed from 'Stopped' to 'Running' (Instance with Web Link)")
    def verifying_if_the_status_has_been_changed_container_with(self):
        return self.wait.until(ec.text_to_be_present_in_element(self.container_with_web_link_status, 'Running'))

    @allure.step("Verifying if the status has been changed from 'Stopped' to 'Running' (Instance without Web Link)")
    def verifying_if_the_status_has_been_changed_container_without(self):
        return self.wait.until(ec.text_to_be_present_in_element(self.container_without_web_link_status, 'Running'))
