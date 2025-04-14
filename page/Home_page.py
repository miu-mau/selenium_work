from .Base_page import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    catalog = {
            "desktop": "http://127.0.0.1:8082/en-gb/catalog/desktops",
            "laptop": "http://127.0.0.1:8082/en-gb/catalog/laptop-notebook",
            "tablet": "http://127.0.0.1:8082/en-gb/catalog/tablet",
            "software": "http://127.0.0.1:8082/en-gb/catalog/software",
            "smartphone": "http://127.0.0.1:8082/en-gb/catalog/smartphone",
            "cameras": "http://127.0.0.1:8082/en-gb/catalog/cameras",
            "mp3" : "http://127.0.0.1:8082/en-gb/catalog/mp3-players",
        }

    def click_catalog(self, product_type):
        time.sleep(1)
        self.click(By.XPATH, f"//a[@href='{self.catalog[product_type]}']")
    def navigate_to_product(self, product_url):
        self.driver.get(product_url)

    def click_logo(self):
        self.click(By.ID, "logo")

    def scroll_down(self, pixels):
        self.scroll_to(0, pixels)

    def scroll_up(self, pixels):
        self.scroll_to(pixels, 0) 

    def add_to_wishlist(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_wishlist = product.find_element(By.XPATH, ".//button[@data-bs-toggle='tooltip' and @title='Add to Wish List']")
                add_to_cart_wishlist.click()

    def add_to_compare(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_compare = product.find_element(By.XPATH, ".//button[@data-bs-toggle='tooltip' and @title='Compare this Product']")
                add_to_cart_compare.click()

    def add_to_cart(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            image = product.find_element(By.XPATH, ".//img")
            if image.get_attribute("title") == product_title:
                add_to_cart_button = product.find_element(By.XPATH, ".//button[@data-bs-toggle='tooltip' and @title='Add to Cart']")
                add_to_cart_button.click()

    def search(self, search_term):
        self.send_keys(By.CSS_SELECTOR, ".form-control.form-control-lg", search_term)
        self.click(By.CSS_SELECTOR, ".btn.btn-light.btn-lg") 
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".form-control.form-control-lg").clear()

    def change_currency(self, currency):
        self.click(By.CSS_SELECTOR, ".fa-solid.fa-caret-down")
        self.click(By.XPATH, f"//a[@href='{currency}']")
        time.sleep(1)