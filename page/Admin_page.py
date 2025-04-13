from .Base_page import BasePage
from selenium.webdriver.common.by import By
import time

class AdminPage(BasePage):
    menu_selector = {
            "Catalog": "1",
            "Extensions": "2",
            "Design": "3",
            "Sales": "4",
            "Customers": "5",
            "Marketing": "6",
            "System": "7",
            "Reports": "8"}
    submenu_selector = {
        "Categories": "category",
        "Products": "product",
        "Subscription Plans": "subscription_plan",
        "Filters": "filter",
        "Attributes": "attribute",
        "Attribute Groups": "attribute_group",
        "Options": "option",
        "Manufacturers": "manufacturer",
        "Downloads": "download",
        "Reviews": "review",
        "Information": "information"
    }

    def scroll_down(self, pixels):
        self.scroll_to(0, pixels)

    def scroll_up(self, pixels):
        self.scroll_to(pixels, 0) 

    def navigate_to_admin(self, url):
        self.driver.get("http://127.0.0.1:8082/administration/index.php?route=common/login")

    def login(self, email, password):
        time.sleep(1)        
        self.send_keys(By.ID, "input-username", email)
        self.send_keys(By.ID, "input-password", password)
        self.click(By.CSS_SELECTOR, ".btn.btn-primary")

    def click_navigate(self, menu_item):
        time.sleep(1)
        self.driver.find_element(By.XPATH, f"//a[@href='#collapse-{self.menu_selector[menu_item]}']").click()

    def click_submenu_item(self, submenu_item):
        submenu_url_part = self.submenu_selector[submenu_item]
        submenu_item_element = self.driver.find_element(By.XPATH, f"//a[contains(@href, '{submenu_url_part}')]")
        submenu_item_element.click()

    def add_new(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

    def add_new_category(self, name):
        self.driver.find_element(By.ID, "input-name-1").send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.ID, "input-meta-title-1").send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='#tab-seo']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "input-keyword-0-1").send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    
    def add_new_product(self, name, category, price):
        self.driver.find_element(By.ID, "input-name-1").send_keys(name)
        time.sleep(1) 
        self.driver.find_element(By.ID, "input-meta-title-1").send_keys(name)
        time.sleep(1) 
        self.driver.find_element(By.XPATH, "//a[@href='#tab-data']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "input-model").send_keys(name)
        time.sleep(1) 
        self.driver.execute_script("window.scrollTo(0, 300);")
        time.sleep(2)
        self.driver.find_element(By.ID, "input-price").send_keys(price)
        time.sleep(1) 
        self.driver.execute_script("window.scrollTo(300, 0);")
        time.sleep(1)        
        self.driver.find_element(By.XPATH, "//a[@href='#tab-links']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "input-category").send_keys(category)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='#tab-seo']").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "input-keyword-0-1").send_keys(name)
        time.sleep(1)      
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()   
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-light").click()    