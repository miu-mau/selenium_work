from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


service = Service(executable_path="C:\\Users\\marin\\Documents\\chromedriver.exe")


driver = webdriver.Chrome(service=service)


driver.get("http://localhost:8082")


time.sleep(10)


driver.quit()
