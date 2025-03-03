from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page.Home_page import HomePage
from page.Product_page import ProductPage
from page.Review_page import ReviewPage
import time

service = Service(executable_path="C:\\Users\\marin\\Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    home_page = HomePage(driver)
    product_page = ProductPage(driver)
    review_page = ReviewPage(driver)


    # 1
    home_page.navigate_to_product("http://localhost:8082")
    time.sleep(2)    
    home_page.scroll_down(300)
    time.sleep(2)
    product_page.select_prod("MacBook")
    time.sleep(2)
    product_page.add_to_wishlist()

    # 2
    home_page.click_logo()
    home_page.scroll_down(1000)
    time.sleep(2)
    product_page.select_prod("Canon EOS 5D")
    product_page.select_color('15') 
    home_page.scroll_down(500) 
    product_page.add_to_cart()
    home_page.scroll_up(0)   
    home_page.click_logo()
    time.sleep(1)

    # 3

    home_page.click_catalog("tablet")
    time.sleep(1)
    home_page.scroll_down(200)
    time.sleep(2)
    home_page.add_to_cart("Samsung Galaxy Tab 10.1")
    time.sleep(1)
    home_page.scroll_up(0)  


    # 4
    home_page.click_catalog("smartphone")
    time.sleep(1)
    home_page.scroll_down(200)
    time.sleep(1)
    home_page.add_to_cart("HTC Touch HD")
    time.sleep(2)

    # 5
    product_page.select_prod("iPhone")
    home_page.scroll_down(500)
    time.sleep(2)
    review_page.click_review()
    home_page.scroll_down(800)
    time.sleep(2)
    review_page.write_review("lalalal", "I like this phone so much", 5)
    time.sleep(2)

finally:
    driver.quit()