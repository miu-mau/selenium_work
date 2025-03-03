import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path="C:\\Users\\marin\\Documents\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_click_carousel_and_logo(driver):
    driver.get("http://localhost:8082")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "carousel-inner").click()
    time.sleep(2)

    driver.find_element(By.ID, "logo").click()
    time.sleep(2)

    assert driver.current_url == "http://127.0.0.1:8082/en-gb?route=common/home", "URL did not match after clicking logo"

def test_change_currency(driver):
    driver.get("http://localhost:8082")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-caret-down").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='EUR']").click()
    time.sleep(2)
    euro = driver.find_element(By.XPATH, "//a[@href='EUR']")
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-caret-down").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='USD']").click()
    time.sleep(2)

    assert driver.find_element(By.XPATH, "//a[@href='USD']") != euro, "Currency did not change to Dollar"

def test_navigate_to_software_catalog(driver):
    driver.get("http://localhost:8082")
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb/catalog/software']").click()
    time.sleep(2)

    assert driver.current_url == "http://127.0.0.1:8082/en-gb/catalog/software", "URL did not match after navigating to software catalog"

    driver.find_element(By.ID, "logo").click()
    time.sleep(2)

def test_register_new_user(driver):
    driver.get("http://localhost:8082")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-user").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb?route=account/register']").click()
    time.sleep(2)
    driver.find_element(By.ID, "input-firstname").send_keys("Lala")
    time.sleep(1)
    driver.find_element(By.ID, "input-lastname").send_keys("LanLan")
    time.sleep(1)
    driver.find_element(By.ID, "input-email").send_keys("lala@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "input-password").send_keys("password")
    time.sleep(1)
    driver.find_element(By.NAME, "agree").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".col-3.d-none.d-md-block").click()

    assert "Your Account Has Been Created!" in driver.page_source, "Registration was not successful"

    time.sleep(2)
    driver.find_element(By.ID, "logo").click()
    time.sleep(2)


def test_search_for_item(driver):
    driver.get("http://localhost:8082")
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, ".form-control.form-control-lg").send_keys("Search")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(2)

    assert driver.find_element(By.ID, "content"), "No search results were found"
    
    driver.find_element(By.ID, "logo").click()
    time.sleep(2)

if __name__ == "__main__":
    pytest.main()