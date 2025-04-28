import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_add_elem(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/add_remove_elements/']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@onclick='addElement()']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']").click()
    time.sleep(1)
    assert len(driver.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")) == 0
    time.sleep(1)

@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_checkbox(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/checkboxes']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, "//input[@type='checkbox']").is_selected()

@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_dropdown(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/dropdown']").click()
    time.sleep(1)
    driver.find_element(By.ID, "dropdown").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//option[@value='1']").click()
    time.sleep(1)
    assert driver.find_element(By.XPATH, "//option[@value='1']").is_selected()
    time.sleep(1)

@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_horizontal(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/horizontal_slider']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type='range']").click()
    time.sleep(1)


@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_menu(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/jqueryui/menu']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='#']")
    time.sleep(1)


@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_scroll(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/infinite_scroll']").click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 800);")
    time.sleep(2)



@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_inputs(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/inputs']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@type='number']").send_keys(19)
    time.sleep(1)


@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_key_press(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/key_presses']").click()
    time.sleep(1)
    driver.find_element(By.ID, "target").send_keys("hello world")
    time.sleep(1)

@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_js_alerts(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/javascript_alerts']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
    time.sleep(3)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(1)

@pytest.mark.parametrize("page_to_open", ["internet"], indirect=True)
def test_enrty_add(driver):
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/entry_ad']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//p[text()='Close']").click()
    time.sleep(1)