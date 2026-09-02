import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from tests.pages.configuration.page_base import PageBase


class SectionStyle(PageBase):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        # Container style
        self.button_card_view = (By.XPATH,
                                 '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[1]/div/button[1]')
        self.button_list_view = (By.XPATH,
                                 '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[1]/div/button[2]')
        self.button_theme_light = (By.XPATH,
                                   '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[2]/div/button[1]')
        self.button_theme_dark = (By.XPATH,
                                  '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[2]/div/button[2]')
        self.button_color_blue_standard = (By.XPATH,
                                           '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[1]')
        self.button_color_blue_ocean = (By.XPATH,
                                        '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[2]')
        self.button_color_green = (By.XPATH,
                                   '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[3]')
        self.button_color_red_alert = (By.XPATH,
                                       '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[4]')
        self.button_color_purple_signal = (By.XPATH,
                                           '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[5]')
        self.button_color_orange_energy = (By.XPATH,
                                           '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[6]')
        self.button_color_white_clean = (By.XPATH,
                                         '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[7]')
        self.button_color_random = (By.XPATH,
                                    '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[3]/div/div/div/button[8]')
        self.button_save_configurations_style_container = (By.XPATH,
                                                           '//*[@id="root"]/div/main/section/div/div/div[3]/div/section/div/div[2]/div[4]/div/button')

    # Clicks !
    @allure.step("Click in button to change card view")
    def click_button_card_view(self):
        self.click(self.button_card_view)

    @allure.step("Click in button to change list view")
    def click_button_list_view(self):
        self.click(self.button_list_view)

    @allure.step("Click in button to put theme light")
    def click_button_theme_light(self):
        self.click(self.button_theme_light)

    @allure.step("Click in button to put theme dark")
    def click_button_theme_dark(self):
        self.click(self.button_theme_dark)

    @allure.step("Click in button to change for color blue standard")
    def click_button_color_blue_standard(self):
        self.click(self.button_color_blue_standard)

    @allure.step("Click in button to change for color blue ocean")
    def click_button_color_blue_ocean(self):
        self.click(self.button_color_blue_ocean)

    @allure.step("Click in button to change for color green")
    def click_button_color_green(self):
        self.click(self.button_color_green)

    @allure.step("Click in button to change for color red alert")
    def click_button_color_red_alert(self):
        self.click(self.button_color_red_alert)

    @allure.step("Click in button to change for color purple signal")
    def click_button_color_purple_signal(self):
        self.click(self.button_color_purple_signal)

    @allure.step("Click in button to change for color orange energy")
    def click_button_color_orange_energy(self):
        self.click(self.button_color_orange_energy)

    @allure.step("Click in button to change for color white clean")
    def click_button_color_white_clean(self):
        self.click(self.button_color_white_clean)

    @allure.step("Click in button to change for color random")
    def click_button_color_random(self):
        self.click(self.button_color_random)

    @allure.step("Click in button to save all configurations")
    def click_button_to_save_configurations(self):
        self.click(self.button_save_configurations_style_container)
