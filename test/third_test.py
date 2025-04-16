import time
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("email, password", [("lala@gmail.com", "password")])
def test_login(pages, email, password):
    home_page, _, _, login_page, _ = pages
    login_page.login(email, password)
    time.sleep(2)
    
    # Проверка, что вход в аккаунт был успешным
    expected_url = "http://127.0.0.1:8082/en-gb?route=account"
    assert home_page.driver.current_url.startswith(expected_url)

    home_page.click_logo()



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
    home_page.click_logo()


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


def test_add_samsung_tablet_to_cart(pages):
    home_page, _, _, _, _ = pages
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
    time.sleep(1)

    time.sleep(2)