from .Base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    def login(self, email, password):
        self.click(By.CSS_SELECTOR, ".fa-solid.fa-user")
        time.sleep(1)
        self.click(By.XPATH, "//a[@href='http://127.0.0.1:8082/en-gb?route=account/login']")
        time.sleep(1)        
        self.send_keys(By.ID, "input-email", email)
        self.send_keys(By.ID, "input-password", password)
        self.click(By.XPATH, "//button[contains(@class, 'btn btn-primary') and text()='Login']")

    def login_rus(self, email, password):
        self.click(By.CSS_SELECTOR, ".fa.fa-user")
        time.sleep(1)
        self.click(By.XPATH, "//a[@href='https://demo-opencart.ru/index.php?route=account/login']")
        time.sleep(1)        
        self.send_keys(By.ID, "input-email", email)
        self.send_keys(By.ID, "input-password", password)
        self.click(By.XPATH, "//input[contains(@class, 'btn btn-primary')]")