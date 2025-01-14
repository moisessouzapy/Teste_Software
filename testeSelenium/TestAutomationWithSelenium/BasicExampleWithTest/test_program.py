import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_path_with_file_name(filename: str) -> str:
    return os.getcwd() + filename

def configure_selenium() -> webdriver:
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(get_path_with_file_name("/Login.html"))
    print("test")
    return driver

def test_email_is_invalid():
    # Assert
    driver: webdriver = configure_selenium()
    element_search_field = driver.find_element(By.ID, "email")
    element_search_field.send_keys("teste1@gmail.com")
    element_password_field = driver.find_element(By.ID, "password")
    element_password_field.send_keys("123456789")
    element_button_submit_search = driver.find_element(By.ID, "signin")

    # Act
    element_button_submit_search.click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    assert element_message_feedback == "Invalid format email!"


def testar_campos_preenchidos():
    # Assert
    driver: webdriver = configure_selenium()
    element_search_field = driver.find_element(By.ID, "email")
    element_search_field.send_keys("")
    element_password_field = driver.find_element(By.ID, "password")
    element_password_field.send_keys("")
    element_button_submit_search = driver.find_element(By.ID, "signin")

    # Act
    element_button_submit_search.click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    assert element_message_feedback == "Username and password will be filled!"



def testar_login_valido():
    # Assert
    driver: webdriver = configure_selenium()
    element_search_field = driver.find_element(By.ID, "email")
    element_search_field.send_keys("test@example.com")
    element_password_field = driver.find_element(By.ID, "password")
    element_password_field.send_keys("123456789")
    element_button_submit_search = driver.find_element(By.ID, "signin")

    # Act
    element_button_submit_search.click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    assert element_message_feedback != "Username or password invalid! :("


def testar_login_invalido():
    # Assert
    driver: webdriver = configure_selenium()
    element_search_field = driver.find_element(By.ID, "email")
    element_search_field.send_keys("moises@gmail.com")
    element_password_field = driver.find_element(By.ID, "password")
    element_password_field.send_keys("987654321")
    element_button_submit_search = driver.find_element(By.ID, "signin")

    # Act
    element_button_submit_search.click()

    # Assert
    element_message_feedback = driver.find_element(By.ID, "messageFeedback").text
    assert element_message_feedback == "Username or password invalid! :("
