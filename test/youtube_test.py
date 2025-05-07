import pytest
from appium import webdriver
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

@pytest.fixture
def driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '11', 
        'deviceName': 'Android Emulator',
        'app': 'C:\\Users\\marin\\Documents\\3курс\\selenium\\youtube.apk', 
        'appWaitActivity': '*.*',
        'automationName': 'UiAutomator2'
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()


def test_tap_search(driver):
    time.sleep(5)
    search_button = driver.find_element_by_accessibility_id("Search")
    pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=pointer)
    actions.pointer_action.move_to(search_button)
    actions.pointer_action.click()
    actions.perform()
    time.sleep(2)
    search_field = driver.find_element_by_id("com.google.android.youtube:id/search_edit_text")
    assert search_field.is_displayed()
    print("tap test passed")


def test_double_tap_video(driver):
    time.sleep(5)
    first_video = driver.find_element_by_id("com.google.android.youtube:id/thumbnail")
    first_video.click()
    time.sleep(5)
    video_player = driver.find_element_by_id("com.google.android.youtube:id/player_view")
    x = video_player.location['x'] + video_player.size['width'] // 2
    y = video_player.location['y'] + video_player.size['height'] // 2
    
    pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=pointer)
    actions.pointer_action.move_to_location(x, y)
    actions.pointer_action.click()
    actions.pointer_action.pause(0.1)
    actions.pointer_action.click()
    actions.perform()
    print("double tap test passed")


def test_long_press_video(driver):
    time.sleep(5)
    first_video = driver.find_element_by_id("com.google.android.youtube:id/thumbnail")
    pointer = PointerInput(interaction.POINTER_TOUCH, "touch")
    actions = ActionBuilder(driver, mouse=pointer)
    actions.pointer_action.move_to(first_video)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(2)
    actions.pointer_action.release()
    actions.perform()
    time.sleep(2)
    save_option = driver.find_element_by_xpath("//*[contains(@text, 'Save') or contains(@text, 'Сохранить')]")
    assert save_option.is_displayed()
    print("long press test passed")


def test_swipe_up(driver):
    time.sleep(5)
    screen_size = driver.get_window_size()
    start_x = screen_size['width'] // 2
    start_y = screen_size['height'] * 3 // 4
    end_y = screen_size['height'] // 4
    driver.swipe(start_x, start_y, start_x, end_y, 800)
    print("swipe test passed")


def test_pinch_video(driver):
    time.sleep(5)
    first_video = driver.find_element_by_id("com.google.android.youtube:id/thumbnail")
    first_video.click()
    time.sleep(5)
    video_player = driver.find_element_by_id("com.google.android.youtube:id/player_view")
    driver.pinch(element=video_player)
    print("pinch test passed")
