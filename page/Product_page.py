from .Base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
    def select_prod(self, product_title):
        products = self.driver.find_elements(By.XPATH, "//div[@class='product-thumb']")      
        for product in products:
            title_element = product.find_element(By.XPATH, ".//h4/a")
            if title_element.text == product_title:
                title_element.click()
                break

    # def select_prod(self, index):
    #     products = [self.mac, self.select_photo, self.samsung]
    #     if index < len(products):
    #         self.click(*products[index])
    #     else:
    #         raise IndexError("Index out of range for product selection.")
    def add_to_wishlist(self):
        self.click(By.XPATH, "//button[@formaction='http://127.0.0.1:8082/en-gb?route=account/wishlist.add']")

    def select_color(self, color_value):
        self.click(By.ID, "input-option-226")
        self.click(By.CSS_SELECTOR, f"[value='{color_value}']")

    def add_to_cart(self):
        self.click(By.ID, "button-cart")
    # def select_prod(self, product_title):
    #     time.sleep(1)
    #     image = self.driver.find_element(By.XPATH, f"//img[@title='{product_title}']")
    #     image.click()