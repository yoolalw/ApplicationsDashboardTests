import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver

class PageAiChat:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.container_chat = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/div/div')

        self.input_message = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/form/div/input')
        self.send_message = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[2]/form/div/button')
        self.clean_chat = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[1]/button')

        