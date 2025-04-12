import allure
import time
from selenium.webdriver.common.by import By

@allure.feature("User  Authentication")
@allure.title("User  Login")
def test_login(pages):
    home_page, _, _, login_page, _ = pages
    login_page.login("lala@gmail.com", "password")
    time.sleep(2)
    
    # Проверка, что вход в аккаунт был успешным
    expected_url = "http://127.0.0.1:8082/en-gb?route=account"
    assert home_page.driver.current_url.startswith(expected_url)

    home_page.click_logo()

@allure.feature("Wishlist")
@allure.title("Add MacBook to Wishlist")
def test_add_macbook_to_wishlist(pages):
    home_page, product_page, _, _, _ = pages
    home_page.scroll_down(300)
    time.sleep(2)
    product_page.select_prod("MacBook")
    time.sleep(2)
    product_page.add_to_wishlist()
    time.sleep(1)
    # Проверка, что MacBook добавлен в вишлист 
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Сообщение об успехе не содержит ожидаемого текста."

    time.sleep(2)

@allure.feature("Shopping Cart")
@allure.story("Add Canon to Cart")
@allure.title("Add Canon EOS 5D to Cart")
def test_add_canon_to_cart(pages):
    home_page, product_page, _, _, _ = pages
    home_page.click_logo()
    home_page.scroll_down(1000)
    time.sleep(2)
    product_page.select_prod("Canon EOS 5D")
    product_page.select_color('15') 
    home_page.scroll_down(500) 
    product_page.add_to_cart()
    time.sleep(1)
    
    # Проверка, что Canon добавлен в корзину
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Сообщение об успехе не содержит ожидаемого текста."

    home_page.scroll_up(0)   
    home_page.click_logo()
    time.sleep(1)

@allure.feature("Shopping Cart")
@allure.story("Add Samsung Tablet to Cart")
@allure.title("Add Samsung Galaxy Tab 10.1 to Cart")
def test_add_samsung_tablet_to_cart(pages):
    home_page, _, _, _, _  = pages
    home_page.click_catalog("tablet")
    time.sleep(1)
    home_page.scroll_down(200)
    time.sleep(2)
    home_page.add_to_cart("Samsung Galaxy Tab 10.1")
    time.sleep(1)
    
    # Проверка, что Samsung Galaxy Tab 10.1 добавлен в корзину
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Сообщение об успехе не содержит ожидаемого текста."

    time.sleep(1)
    home_page.scroll_up(0)

@allure.feature("Shopping Cart")
@allure.story("Add HTC to Cart")
@allure.title("Add HTC Touch HD to Cart")
def test_add_htc_to_cart(pages):
    home_page, _, _, _, _ = pages
    home_page.click_catalog("smartphone")
    time.sleep(1)
    home_page.scroll_down(200)
    time.sleep(1)
    home_page.add_to_cart("HTC Touch HD")
    time.sleep(1)
    
    # Проверка, что HTC Touch HD добавлен в корзину
    success_alert = home_page.driver.find_elements(By.CSS_SELECTOR, ".alert.alert-success")
    assert "Success: You have added" in success_alert[0].text, "Сообщение об успехе не содержит ожидаемого текста."

    

    time.sleep(2)
    home_page.scroll_up(0)

@allure.feature("Review")
@allure.story("Write Review for iPhone")
@allure.title("Write a review for iPhone")
def test_write_review_for_iphone(pages):
    home_page, product_page, review_page, _, _ = pages
    home_page.click_catalog("smartphone")   
    product_page.select_prod("iPhone")
    home_page.scroll_down(500)
    time.sleep(2)
    review_page.click_review()
    home_page.scroll_down(800)
    time.sleep(2)
    review_page.write_review("lalalal", "I like this phone so much", 5)
    time.sleep(2)