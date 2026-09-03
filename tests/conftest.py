
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function', autouse=True)
def driver(request):
    service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait

    driver.implicitly_wait(7)
    driver.maximize_window()

    yield driver
    driver.quit()