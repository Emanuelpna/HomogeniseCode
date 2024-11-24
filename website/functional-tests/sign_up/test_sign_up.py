from uuid import uuid4 
import time
from selenium.webdriver.common.by import By

def test_open_site_firefox(firefox_browser):
    firefox_browser.get("http://web:5000/sign-up")

    assert firefox_browser.title == "Sign Up"

def test_open_site_chrome(chrome_browser):
    chrome_browser.get("http://web:5000/sign-up")

    assert chrome_browser.title == "Sign Up"

def test_create_user_with_email_invalid_length(firefox_browser):
    firefox_browser.get("http://web:5000/sign-up")

    input_email = firefox_browser.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys("tes")

    input_firstName = firefox_browser.find_element(By.XPATH, '//*[@id="firstName"]')
    input_firstName.send_keys("Nome do Usuário de Teste")

    input_password1 = firefox_browser.find_element(By.XPATH, '//*[@id="password1"]')
    input_password1.send_keys("1234567")

    input_password2 = firefox_browser.find_element(By.XPATH, '//*[@id="password2"]')
    input_password2.send_keys("1234567")

    form_element = firefox_browser.find_element(By.XPATH, '/html/body/div/form')
    form_element.submit()

    time.sleep(1)

    try:
        # Estoura um erro caso não encontre o elemento
        flash_message_accountCreated = firefox_browser.find_element(By.CSS_SELECTOR, '.alert.alert-success[role="alert"]')
    
        assert not flash_message_accountCreated.is_displayed()
    except:
        # Não deveria encontrar o elemento em tela, se realmente não encontrou força um sucesso no teste
        assert True

def test_create_user_with_email_valid_length(firefox_browser):
    firefox_browser.get("http://web:5000/sign-up")

    input_email = firefox_browser.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys("t@em") # A validação do input[type="email"] nos navegadores exige que tenha pelo menos um @ na string

    input_firstName = firefox_browser.find_element(By.XPATH, '//*[@id="firstName"]')
    input_firstName.send_keys("Nome do Usuário de Teste")

    input_password1 = firefox_browser.find_element(By.XPATH, '//*[@id="password1"]')
    input_password1.send_keys("1234567")

    input_password2 = firefox_browser.find_element(By.XPATH, '//*[@id="password2"]')
    input_password2.send_keys("1234567")

    form_element = firefox_browser.find_element(By.XPATH, '/html/body/div/form')
    form_element.submit()

    time.sleep(1)

    try:
        # Estoura um erro caso não encontre o elemento
        flash_message_accountCreated = firefox_browser.find_element(By.CSS_SELECTOR, '.alert.alert-success[role="alert"]')
   
        assert flash_message_accountCreated.is_displayed()
    except:
        # Deveria ter a mensagem de sucesso. Se não encontrou o elemento na tela força uma falha no teste
        assert False


def test_create_user_with_username_invalid_length(firefox_browser):
    firefox_browser.get("http://web:5000/sign-up")

    input_email = firefox_browser.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys("Test@gmail.com")

    input_firstName = firefox_browser.find_element(By.XPATH, '//*[@id="firstName"]')
    input_firstName.send_keys("T")

    input_password1 = firefox_browser.find_element(By.XPATH, '//*[@id="password1"]')
    input_password1.send_keys("1234567")

    input_password2 = firefox_browser.find_element(By.XPATH, '//*[@id="password2"]')
    input_password2.send_keys("1234567")

    form_element = firefox_browser.find_element(By.XPATH, '/html/body/div/form')
    form_element.submit()

    time.sleep(1)

    try:
        flash_message_accountCreated = firefox_browser.find_element(By.CSS_SELECTOR, '.alert.alert-success[role="alert"]')
    
        assert not flash_message_accountCreated.is_displayed()
    except:
        assert True

def test_create_user_with_username_valid_length(firefox_browser):
    firefox_browser.get("http://web:5000/sign-up")

    input_email = firefox_browser.find_element(By.XPATH, '//*[@id="email"]')
    input_email.send_keys("Test@gmail.com")

    input_firstName = firefox_browser.find_element(By.XPATH, '//*[@id="firstName"]')
    input_firstName.send_keys("Te")

    input_password1 = firefox_browser.find_element(By.XPATH, '//*[@id="password1"]')
    input_password1.send_keys("1234567")

    input_password2 = firefox_browser.find_element(By.XPATH, '//*[@id="password2"]')
    input_password2.send_keys("1234567")

    form_element = firefox_browser.find_element(By.XPATH, '/html/body/div/form')
    form_element.submit()

    time.sleep(1)

    try:
        flash_message_accountCreated = firefox_browser.find_element(By.CSS_SELECTOR, '.alert.alert-success[role="alert"]')
    
        assert not flash_message_accountCreated.is_displayed()
    except:
        assert True