from uuid import uuid4 
import time
from selenium.webdriver.common.by import By

def test_open_site_firefox(firefox_browser):
    firefox_browser.get("http://web:5000/sign-up")

    assert firefox_browser.title == "Sign Up"

def test_open_site_chrome(chrome_browser):
    chrome_browser.get("http://web:5000/sign-up")

    assert chrome_browser.title == "Sign Up"
