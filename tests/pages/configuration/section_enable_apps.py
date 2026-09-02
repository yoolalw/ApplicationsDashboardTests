import allure
from selenium.webdriver.common.by import By
from tests.pages.configuration.page_base import PageBase
class SectionEnableApps(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        # Principal container
        self.container_principal = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]')
        # First div present
        self.button_disable_app = (By.XPATH,
                                   '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[2]/div[2]/button[1]')
        self.button_edit_app = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[2]/div[2]/button[2]')
        self.button_delete_app = (By.XPATH,
                                  '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[2]/div[2]/button[3]')
        self.status_application = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[2]/span')

    @allure.step("Verifying if the container has present")
    def verifying_displayed_container(self):
        return self.displayed(self.container_principal)

    @allure.step("Click in disable instance button")
    def click_in_button_disable(self):
        self.click(self.button_disable_app)

    @allure.step("Click in edit instance button")
    def click_in_button_disable(self):
        self.click(self.button_edit_app)

    @allure.step("Click in delete instance button")
    def click_in_button_disable(self):
        self.click(self.button_delete_app)

    @allure.step("Checking text returned after click in button")
    def check_text_returned(self):
        return self.text(self.status_application)