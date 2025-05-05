import pytest
from appium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.android.calculator2",
        "appActivity": "com.android.calculator2.Calculator"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

def click(driver, id_):
    driver.find_element(By.ID, id_).click()

def get_result(driver):
    return driver.find_element(By.ID, "com.android.calculator2:id/result").text

def test_addition(driver):
    click(driver, "com.android.calculator2:id/digit_2")
    click(driver, "com.android.calculator2:id/op_add")
    click(driver, "com.android.calculator2:id/digit_3")
    click(driver, "com.android.calculator2:id/eq")
    assert get_result(driver) == "5"

def test_subtraction(driver):
    click(driver, "com.android.calculator2:id/digit_7")
    click(driver, "com.android.calculator2:id/op_sub")
    click(driver, "com.android.calculator2:id/digit_4")
    click(driver, "com.android.calculator2:id/eq")
    assert get_result(driver) == "3"

def test_multiplication(driver):
    click(driver, "com.android.calculator2:id/digit_6")
    click(driver, "com.android.calculator2:id/op_mul")
    click(driver, "com.android.calculator2:id/digit_3")
    click(driver, "com.android.calculator2:id/eq")
    assert get_result(driver) == "18"

def test_division(driver):
    click(driver, "com.android.calculator2:id/digit_8")
    click(driver, "com.android.calculator2:id/op_div")
    click(driver, "com.android.calculator2:id/digit_2")
    click(driver, "com.android.calculator2:id/eq")
    assert get_result(driver) == "4"

def test_complex(driver):
    click(driver, "com.android.calculator2:id/digit_5")
    click(driver, "com.android.calculator2:id/op_mul")
    click(driver, "com.android.calculator2:id/digit_5")
    click(driver, "com.android.calculator2:id/op_sub")
    click(driver, "com.android.calculator2:id/digit_1")
    click(driver, "com.android.calculator2:id/eq")
    assert get_result(driver) == "24"
