import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page_home import PageHome

from tests.conftest import driver


@pytest.mark.usefixtures("driver")
class TestHomePageNegative:
    driver: WebDriver
    wait: WebDriverWait

    def setup_method(self):
        self.driver.get('http://127.0.0.1:3000/')
        self.page_home = PageHome(self.driver)


    @pytest.mark.parametrize(
        "name, port, directory, command, arguments", [
            ("ifjoaifhjsdiufhsdifhisdpfjisoihjiodhfgishgifdsh9 83uif908uf09", "309siudfh",
             "kfjghskldjghdsfgh9orhsje09438593", "ofigjsoiughsdiughsdfog", "SLDKJFHNLFIUGHSD"),
            ("ifjoaifhjsdiufhsdifhisdpfjisoihjiodhfgishgifdsh9 83uif908uf09", "309siudfh",
             "kfjghskldjghdsf343443443433gh9orhsje09438593", "ofgfdsgfgf2312314igjsoiughsdiughsdfog",
             "SLDKJFHNLFDFGFDFGFDGDFSgffsgsdIUGHSD"),
            ("11111111111111111", "11111111111", "1111111111111111111", "111111111111111111111111", "111111111111111"),
            ("", "", "", "", ""),
            ("-1", "-2", "-3", "-4", "-5"),
        ]
    )
    @allure.title("Inserting values for negative tests - Creating new application")
    def test_inserting_not_common_data_in_new_applications_container(self, name, port, directory, command, arguments):
        self.page_home.click_on_new_app_button()
        self.page_home.creating_new_application(name, port, directory, command, arguments)
        self.page_home.click_in_new_app_add_app_button()
        assert False

