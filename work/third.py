from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
import time

service = Service(executable_path="C:\\Users\\marin\\Documents\\chromedriver.exe") 
driver = webdriver.Chrome(service=service)

try: 
    driver.get("http://localhost:8082") 
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 300);")
    time.sleep(2)
    select_prod = driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb/product/macbook']")
    select_prod.click()
    time.sleep(2)
    wishlist = driver.find_element(By.XPATH, "//button[@formaction='http://127.0.0.1:8082/en-gb?route=account/wishlist.add']")
    wishlist.click()
    time.sleep(3)

    logo = driver.find_element(By.ID, "logo")
    logo.click()
    time.sleep(2)

    # 2
    driver.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)
    select_photo = driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb/product/canon-eos-5d']")
    select_photo.click()
    time.sleep(2)
    color = driver.find_element(By.ID, "input-option-226")
    color.click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 500);")
    color_red = driver.find_element(By.CSS_SELECTOR, "[value='15']")
    color_red.click()
    time.sleep(2)
    add_to_cart = driver.find_element(By.ID, "button-cart")
    add_to_cart.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(2)    
    logo = driver.find_element(By.ID, "logo")
    logo.click()
    time.sleep(2)

    # 3
    tab = driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb/catalog/tablet']")
    tab.click()
    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(2)
    samsung = driver.find_element(By.XPATH, "//button[@formaction='http://127.0.0.1:8082/en-gb?route=checkout/cart.add']")
    samsung.click()
    driver.execute_script("window.scrollTo(200, 0)")
    time.sleep(2)
    logo = driver.find_element(By.ID, "logo")
    logo.click()
    time.sleep(3)

    # 4
    phone = driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb/catalog/smartphone']")
    phone.click()
    driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(2)
    htc = driver.find_element(By.XPATH, "//button[@formaction='http://127.0.0.1:8082/en-gb?route=checkout/cart.add']")
    htc.click()
    time.sleep(2)

    # 5
    time.sleep(2)
    iphone = driver.find_element(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb/product/smartphone/iphone']")
    iphone.click()
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(3)
    review = driver.find_element(By.XPATH, "//a[@href='#tab-review']")
    review.click()
    time.sleep(2)
    write_name = driver.find_element(By.ID, "input-name")
    write_name.send_keys("lalalal")
    text_rew = driver.find_element(By.ID, "input-text")
    text_rew.send_keys("i like this phone so much")
    driver.execute_script("window.scrollTo(0, 800);")
    time.sleep(2)
    value_5 = driver.find_element(By.CSS_SELECTOR, "[value='5']")
    value_5.click()
    time.sleep(2)

    cont = driver.find_element(By.ID, "button-review")
    cont.click()
    time.sleep(2)
finally: 
    driver.quit()