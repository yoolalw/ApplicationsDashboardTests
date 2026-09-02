import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from tests.pages.configuration.page_base import PageBase


class SectionAdvancedResources(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # Container advanced resources
        self.button_enable_ai_chat = (By.XPATH,
                                      '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[1]')
        self.button_enable_api_tester = (By.XPATH,
                                         '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[4]')
        self.button_enable_tests_and_connectivity = (By.XPATH,
                                                     '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[4]')
        self.button_enable_mini_server_web = (By.XPATH,
                                              '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[4]')
        self.button_enable_scripts = (By.XPATH,
                                      '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[5]')
        self.button_enable_central_alerts = (By.XPATH,
                                             '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[1]/div[2]/label[3]')

            # Ai Chat configuration
        self.select_open_ai_provider = (By.XPATH,
                                        '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/div/label[1]/select')
        self.select_options = (By.XPATH,
                               '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/div/label[1]/select/option')
        self.input_model_ai = (By.XPATH,
                               '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/label[1]/input')
        self.input_base_url_customized = (By.XPATH,
                                          '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/section[2]/div[2]/label[2]/input')
        self.button_save_configurations_adv_resources_container = (By.XPATH,
                                                                   '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div/button')

    # Click !

    @allure.step("Click in button to enable ai chat")
    def click_in_button_ai_chat(self):
        self.click(self.button_enable_ai_chat)

    @allure.step("Click in button to enable api tester")
    def click_in_button_enable_api_tester(self):
        self.click(self.button_enable_api_tester)

    @allure.step("Click in button to enable mini server web ")
    def click_in_button_mini_server_web(self):
        self.click(self.button_enable_mini_server_web)

    @allure.step("Click in button to enable scripts")
    def click_in_button_scripts(self):
        self.click(self.button_enable_scripts)

    @allure.step("Click in button enable central alerts")
    def click_in_button_central_alerts(self):
        self.click(self.button_enable_central_alerts)

    @allure.step("Click in button to save all configurations")
    def click_button_save_configurations(self):
        self.click(self.button_save_configurations_adv_resources_container)

    # Select !
    @allure.step("Selecting options in Ai Provider container")
    def select_options_in_ai_provider_container(self):
        select_element = self.wait.until(expected_conditions.visibility_of_element_located(self.select_open_ai_provider))
        select = Select(select_element)
        return select


    # Input !

    @allure.step("Inserting values in field Model Ai")
    def inserting_values_in_field_model_ai(self, value):
        self.fill(self.input_model_ai, value)

    @allure.step("Inserting values in field Base Url Customized")
    def inserting_values_in_customized_base_url_ai(self, value):
        self.fill(self.input_base_url_customized, value)

