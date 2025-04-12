from .Base_page import BasePage
from selenium.webdriver.common.by import By
import time

class AdminPage(BasePage):
    def navigate_to_admin(self, url):
        self.driver.get(url)

    def login(self, email, password):
        time.sleep(1)        
        self.send_keys(By.ID, "input-username", email)
        self.send_keys(By.ID, "input-password", password)
        self.click(By.CSS_SELECTOR, ".btn.btn-primary")

    def click_navigate(self, menu_item):
        time.sleep(1)
        menu_selector = f"//a[contains(text(), '{menu_item}')]"
        self.driver.find_element(By.XPATH, menu_selector).click()
        time.sleep(1)

    def click_submenu(self, submenu_item):
        time.sleep(1)
        submenu_selector = f"//a[contains(text(), '{submenu_item}')]"
        self.driver.find_element(By.XPATH, submenu_selector).click()
