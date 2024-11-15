import pytest
from selenium import webdriver

@pytest.fixture()  
def firefox_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument("--incognito")
    driver = webdriver.Remote('http://selenium-hub:4444/wd/hub', options=options)

    driver.implicitly_wait(10)  

    yield driver  

    driver.quit()

@pytest.fixture()  
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Remote('http://selenium-hub:4444/wd/hub', options=options)

    driver.implicitly_wait(10)  

    yield driver  

    driver.quit()