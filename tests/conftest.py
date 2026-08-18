
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function', autouse=True)
def driver(request):
    service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait

    driver.implicitly_wait(5)

    yield driver
    driver.quit()