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
        self.name_application = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[2]/div[1]/p[1]')
        self.cmd_and_args_application = (By.XPATH, '//*[@id="root"]/div/main/section/div/div/div[3]/div/div[2]/div[1]/p[2]')
        self.button_to_save_new_configuration = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[2]/button[2]')
        # Container for insert new values in container (Edit Container)
        self.container_edit_input_application_name = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section/div/label[1]/input')
        self.container_edit_input_command = (By.XPATH,' //*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section/div/label[3]/input')
        self.container_edit_input_arguments = (By.XPATH, '//*[@id="root"]/div/main/section/div[2]/aside/form/div[1]/section/div/label[4]/input')


    @allure.step("Verifying if the container has present")
    def verifying_displayed_container(self):
        return self.displayed(self.container_principal)

    @allure.step("Click in disable instance button")
    def click_in_button_disable(self):
        self.click(self.button_disable_app)

    @allure.step("Click in edit instance button")
    def click_in_button_edit(self):
        self.click(self.button_edit_app)

    @allure.step("Click in delete instance button")
    def click_in_button_delete(self):
        self.click(self.button_delete_app)

    @allure.step("Click in button to save the new configuration")
    def click_in_button_save_configuration(self):
        self.click(self.button_to_save_new_configuration)

    @allure.step("Checking text returned after click in button")
    def check_text_returned(self):
        return self.text(self.status_application)

    @allure.step("Checking text returned after edit the name from the application")
    def check_text_returned_in_name_application(self):
        return self.text(self.name_application)

    @allure.step("Checking text returned after edit the commands and arguments from the application")
    def check_text_returned_in_cmd_and_arg_application(self):
        return self.text(self.name_application)

    @allure.step("Inserting new values in 'Application Name'")
    def insert_new_values_in_app_name(self, value):
        self.fill(self.container_edit_input_application_name, value)

    @allure.step("Inserting new values in 'Command'")
    def insert_new_values_in_command(self, value):
        self.fill(self.container_edit_input_command, value)

    @allure.step("Inserting new values in 'Arguments'")
    def insert_new_values_in_arguments(self, value):
        self.fill(self.container_edit_input_arguments, value)
