import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.configuration.page_base import PageBase


class SectionLogs(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # Container log
        self.button_download_logs = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[1]/button')

    @allure.step("Click in button to download the logs")
    def click_to_download_logs(self):
        self.click(self.button_download_logs)
