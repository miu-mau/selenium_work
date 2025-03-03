from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path="C:\\Users\\marin\\Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://localhost:8082")
    time.sleep(2)

    # 1
    element = driver.find_element(By.CLASS_NAME, "carousel-inner")
    element.click()
    time.sleep(2)
    logo = driver.find_element(By.ID, "logo")
    logo.click()
    time.sleep(2)

    #  2
    money = driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-caret-down")
    money.click()
    time.sleep(1)
    euro = driver.find_element(By.XPATH, "//a[@href='EUR']")
    euro.click()
    time.sleep(2)
    money = driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-caret-down")
    money.click()
    time.sleep(1)
    dollar = driver.find_element(By.XPATH, "//a[@href='USD']")
    dollar.click()
    time.sleep(2)

    # 3
    software = driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb/catalog/software']")
    software.click()
    time.sleep(2)
    logo = driver.find_element(By.ID, "logo")
    logo.click()
    time.sleep(2)

    # 3
    user = driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-user")
    user.click()
    time.sleep(1)
    register = driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb?route=account/register']")
    register.click()
    time.sleep(2)
    first = driver.find_element(By.ID, "input-firstname")
    first.send_keys("Lala")
    time.sleep(1)
    last = driver.find_element(By.ID, "input-lastname")
    last.send_keys("LanLan")
    time.sleep(1)
    email = driver.find_element(By.ID, "input-email")
    email.send_keys("lala@gmail.com")
    time.sleep(1)
    password = driver.find_element(By.ID, "input-password")
    password.send_keys("password")
    time.sleep(1)
    privacy = driver.find_element(By.NAME, "agree")
    privacy.click()
    time.sleep(1)
    confirm = driver.find_element(By.CSS_SELECTOR, ".col-3.d-none.d-md-block")
    confirm.click()
    time.sleep(2)
    logo = driver.find_element(By.ID, "logo")
    logo.click()
    time.sleep(2)

    # 4
    text_search = driver.find_element(By.CSS_SELECTOR, ".form-control.form-control-lg")
    text_search.send_keys("Search")
    time.sleep(1)
    search = driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg")
    search.click()
    time.sleep(2)
    logo = driver.find_element(By.ID, "logo")
    logo.click()
    time.sleep(2)

finally:
    driver.quit()
